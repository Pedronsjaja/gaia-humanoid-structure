"""Verifica integridade dos arquivos recebidos, sem dependências externas."""
from pathlib import Path
import hashlib
import json
import sys


def verificar(root):
    erros = []
    conferidos = 0
    manifests = [
        (root / 'hardware/manifest.json', root / 'hardware', 'file'),
        (root / 'docs/projeto/manifest.json', root, 'destino'),
    ]
    for manifest, base, campo in manifests:
        data = json.loads(manifest.read_text(encoding='utf-8'))
        records = data['arquivos'] if isinstance(data, dict) else data
        for record in records:
            path = (base / record[campo]).resolve()
            if not path.is_relative_to(root.resolve()):
                erros.append(f'Caminho fora do projeto: {record[campo]}')
                continue
            if not path.is_file():
                erros.append(f'Ausente: {record[campo]}')
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if path.stat().st_size != record['bytes'] or digest != record['sha256']:
                erros.append(f'Conteúdo divergente: {record[campo]}')
            conferidos += 1
    return conferidos, erros


if __name__ == '__main__':
    try:
        count, errors = verificar(Path(__file__).resolve().parents[1])
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Falha ao ler inventário: {exc}', file=sys.stderr)
        sys.exit(1)
    for error in errors:
        print(error, file=sys.stderr)
    print(f'{count} registros conferidos; {len(errors)} divergências.')
    sys.exit(1 if errors else 0)
