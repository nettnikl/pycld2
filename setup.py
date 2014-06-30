#!/usr/bin/env python

#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from distutils.core import setup, Extension
import distutils.core
import platform
import subprocess
import sys
import os
import glob

CLD2_PATH = 'cld2'
BIND_PATH = 'bindings'

# Test suite
class cldtest(distutils.core.Command):
    # user_options, initialize_options and finalize_options must be overriden.
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call([sys.executable, 'tests/cld_test.py'])
        raise SystemExit(errno)

src_files = glob.glob(CLD2_PATH+'/internal/*.cc') + ['%s/pycldmodule.cc' % BIND_PATH, '%s/encodings.cc' % BIND_PATH]


cld_files = ['cldutil.cc', 'cldutil_shared.cc', 'compact_lang_det.cc',
             'compact_lang_det_hint_code.cc', 'compact_lang_det_impl.cc',
             'debug.cc', 'fixunicodevalue.cc', 'generated_entities.cc',
             'generated_language.cc', 'generated_ulscript.cc',
             'getonescriptspan.cc', 'lang_script.cc', 'offsetmap.cc',
             'scoreonescriptspan.cc', 'tote.cc', 'utf8statetable.cc',
             'cld_generated_cjk_uni_prop_80.cc', 'cld2_generated_cjk_compatible.cc',
             'cld_generated_cjk_delta_bi_32.cc', 'generated_distinct_bi_0.cc',
             'cld2_generated_quad0122.cc', 'cld2_generated_deltaocta0122.cc',
             'cld2_generated_distinctocta0122.cc',
             'cld_generated_score_quad_octa_0122.cc']

src_files = ['{}/internal/{}'.format(CLD2_PATH, f) for f in cld_files]

src_files.extend(['%s/pycldmodule.cc' % BIND_PATH, '%s/encodings.cc' % BIND_PATH])

module = Extension('pycld2.pycld2',
                   language='c++',
                   extra_compile_args=['-w', '-O2', '-m64', '-fPIC'],
                   include_dirs = ['%s/public' % CLD2_PATH,
                                   '%s/internal' % CLD2_PATH],
                   libraries = [],
                   sources=src_files,
                   )

setup(name='pycld2',
      version='0.1',
      author='Michael McCandless',
      author_email='mail@mikemccandless.com',
      description='Python bindings around Google Chromium\'s embedded compact language detection library (CLD2)',
      ext_modules = [module],
      license = 'Apache2',
      url = 'http://code.google.com/p/chromium-compact-language-detector/',
      classifiers = [
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic'
        ],
      packages=["pycld2"],
      )