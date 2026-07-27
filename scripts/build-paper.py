"""Build PDF from paper markdown via Pandoc+XeLaTeX with Unicode math preprocessing.
Usage: python build-paper.py <paper.md>
Output: <paper.pdf> in same directory.
KIF-27 compliance: checks for U+FFFD replacement characters after build."""
import re, subprocess, os, sys

def build_pdf(md_path):
    base = os.path.splitext(md_path)[0]
    pdf_path = base + '.pdf'
    build_path = base + '.build.md'

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) >= 3:
        yaml_header = parts[1]
        body = parts[2]
        # A2: Strip keywords YAML before Pandoc build
        yaml_header = re.sub(r'\nkeywords:\n(?:  - .+\n)+', '', yaml_header)
        yaml_header = re.sub(r'\nkeywords:.*\n', '', yaml_header)

        # A1: Unicode->LaTeX math preprocessor
        math_blocks = []
        def save_math(m):
            math_blocks.append(m.group(0))
            return f'<<<MATH{len(math_blocks)-1}>>>'
        body = re.sub(r'\$\$[^$]+\$\$', save_math, body)
        body = re.sub(r'\$[^$]+\$', save_math, body)

        greek = {'α':'\\alpha','ω':'\\omega','φ':'\\phi','π':'\\pi',
                 'ℚ':'\\mathbb{Q}','ℝ':'\\mathbb{R}','ℂ':'\\mathbb{C}','ℤ':'\\mathbb{Z}'}
        for uni, latex in greek.items():
            body = body.replace(uni, '$' + latex + '$')
        symbols = {'⊗':'\\otimes','×':'\\times','≈':'\\approx',
                   '≥':'\\ge','≤':'\\le','⟨':'\\langle','⟩':'\\rangle'}
        for uni, latex in symbols.items():
            body = body.replace(uni, '$' + latex + '$')
        body = body.replace('\u2212', '-')  # minus sign
        for sub, d in {'\u2080':'0','\u2081':'1','\u2082':'2','\u2083':'3','\u2084':'4','\u2085':'5','\u2086':'6','\u2087':'7','\u2088':'8','\u2089':'9'}.items():
            body = body.replace(sub, '_{' + d + '}')
        for sup, d in {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4','\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9'}.items():
            body = body.replace(sup, '^{' + d + '}')
        for i, block in enumerate(math_blocks):
            body = body.replace(f'<<<MATH{i}>>>', block)
        content = '---' + yaml_header + '---' + body

    with open(build_path, 'w', encoding='utf-8') as f:
        f.write(content)

    result = subprocess.run(
        ['pandoc', build_path, '-o', pdf_path, '--pdf-engine=xelatex'],
        capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(md_path))
    )

    os.remove(build_path)

    if result.returncode != 0:
        print(f'PANDOC FAILED:\n{result.stderr}')
        sys.exit(1)

    # KIF-27: verify no U+FFFD
    import fitz
    doc = fitz.open(pdf_path)
    errors = [p.number for p in doc if '\ufffd' in p.get_text()]
    if errors:
        for pn in errors[:5]:
            for line in doc[pn].get_text().split('\n'):
                if '\ufffd' in line:
                    print(f'REPLACEMENT CHAR p{pn}: {line.strip()[:120]}')
        print(f'BLOCKED: PDF contains U+FFFD on {len(errors)} pages')
        sys.exit(1)

    print(f'OK: {len(doc)} pages, CLEAN')
    print(f'PDF: {pdf_path}')
    return pdf_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python build-paper.py <paper.md>')
        sys.exit(1)
    build_pdf(sys.argv[1])
