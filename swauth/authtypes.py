# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# Pablo Llopis 2011

import hashlib

class Plaintext(object):
    def encode(self, key):
        return "plaintext:%s" % key

    def match(self, key, creds):
        return self.encode(key) == creds

class Sha1(object):
    def encode(self, key):
        enc_key = '%s%s' % (self.salt, key)
        enc_val = hashlib.sha1(enc_key).hexdigest()
        return "sha1:%s$%s" % (self.salt, enc_val)

    def match(self, key, creds):
        return self.encode(key) == creds
