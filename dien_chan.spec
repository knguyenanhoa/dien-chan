# -*- mode: python -*-

import sys
site_packages = [path for path in sys.path if 
path.rstrip("/\\").endswith('site-packages')]
print("site_packages:", site_packages)

from kivy.tools.packaging.pyinstaller_hooks import get_deps_all, hookspath, runtime_hooks

block_cipher = None

added_files = [(site_packages_, ".") for site_packages_ in site_packages]

kwargs = get_deps_all()
kwargs["datas"] = added_files
kwargs["hiddenimports"] += ['queue', 'unittest', 'unittest.mock']

a = Analysis(['main.py'],
             pathex=['/Volumes/untitled 1/dien_chan'],
             binaries=None,
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             **kwargs)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='dien_chan',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe, Tree('/Volumes/untitled 1/dien_chan/'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='dienChan')
app = BUNDLE(coll,
             name='dienChanFinal.app',
             icon=None,
             bundle_identifier=None)
