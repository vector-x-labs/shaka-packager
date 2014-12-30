# Copyright 2014 Google Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

{
  'variables': {
    # Scan ca bundle in its common appearing locations.
    'curl_ca_bundle%':
      '<!(for path in /etc/pki/tls/certs/ca-bundle.crt       \
                      /etc/ssl/cert.pem                      \
                      /etc/ssl/certs/ca-bundle.crt           \
                      /etc/ssl/certs/ca-certificates.crt     \
                      /usr/local/share/certs/ca-root.crt     \
                      /usr/share/ssl/certs/ca-bundle.crt; do \
            if test -f "$path"; then ca="$path"; break; fi;  \
          done;                                              \
          if [ -z "$ca" ]; then                              \
            echo "Failed to locate SSL CA cert."; exit 1;    \
          else                                               \
            echo "$ca";                                      \
          fi)',
  },
  'targets': [
    {
      'target_name': 'curl_config',
      'type': '<(component)',
      'sources': [
        'config/curl/curlbuild.h',
      ],
      'direct_dependent_settings': {
        'defines': [
          'HTTP_ONLY',
          'USE_IPV6',
          'USE_OPENSSL'
          'USE_SSLEAY',
          'CURL_CA_BUNDLE="<(curl_ca_bundle)"',
        ],
        'include_dirs': [
          'config',
          'config/curl',
        ],
        'direct_dependent_settings': {
          'include_dirs': [
            'config/curl',
          ],
        },
      },
      'conditions': [
        ['OS == "linux"', {
          'sources': [
            'config/linux/curl_config.h',
          ],
          'direct_dependent_settings': {
            'defines': [
              'HAVE_CONFIG_H',
            ],
            'include_dirs': [
              'config/linux',
            ],
          },
        }],
        ['OS == "win"', {
          'direct_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-lws2_32.lib',
              ],
            },
          },
        }],
      ],
    },
    {
      'target_name': 'libcurl',
      'type': '<(component)',
      'conditions': [
        ['_type == "static_library"', {
          'defines': [
            'CURL_STATICLIB',
          ],
        }],
      ],
      'include_dirs': [
        'source/lib',
        'source/include',
      ],
      'dependencies': [
        '../openssl/openssl.gyp:openssl',
        '../zlib/zlib.gyp:zlib',
        'curl_config',
      ],
      'direct_dependent_settings': {
        'conditions': [
          ['_type == "static_library"', {
            'defines': [
              'CURL_STATICLIB',
            ],
          }],
        ],
        'include_dirs': [
          'source/include',
        ],
      },
      'sources': [
        'source/lib/amigaos.c',
        'source/lib/asyn-ares.c',
        'source/lib/asyn-thread.c',
        'source/lib/base64.c',
        'source/lib/bundles.c',
        'source/lib/conncache.c',
        'source/lib/connect.c',
        'source/lib/content_encoding.c',
        'source/lib/cookie.c',
        'source/lib/curl_addrinfo.c',
        'source/lib/curl_fnmatch.c',
        'source/lib/curl_gethostname.c',
        'source/lib/curl_gssapi.c',
        'source/lib/curl_memrchr.c',
        'source/lib/curl_multibyte.c',
        'source/lib/curl_ntlm.c',
        'source/lib/curl_ntlm_core.c',
        'source/lib/curl_ntlm_msgs.c',
        'source/lib/curl_ntlm_wb.c',
        'source/lib/curl_rtmp.c',
        'source/lib/curl_sasl.c',
        'source/lib/curl_sspi.c',
        'source/lib/curl_threads.c',
        'source/lib/dict.c',
        'source/lib/dotdot.c',
        'source/lib/easy.c',
        'source/lib/escape.c',
        'source/lib/file.c',
        'source/lib/fileinfo.c',
        'source/lib/formdata.c',
        'source/lib/ftp.c',
        'source/lib/ftplistparser.c',
        'source/lib/getenv.c',
        'source/lib/getinfo.c',
        'source/lib/gopher.c',
        'source/lib/hash.c',
        'source/lib/hmac.c',
        'source/lib/hostasyn.c',
        'source/lib/hostcheck.c',
        'source/lib/hostip.c',
        'source/lib/hostip4.c',
        'source/lib/hostip6.c',
        'source/lib/hostsyn.c',
        'source/lib/http.c',
        'source/lib/http_chunks.c',
        'source/lib/http_digest.c',
        'source/lib/http_negotiate.c',
        'source/lib/http_negotiate_sspi.c',
        'source/lib/http_proxy.c',
        'source/lib/idn_win32.c',
        'source/lib/if2ip.c',
        'source/lib/imap.c',
        'source/lib/inet_ntop.c',
        'source/lib/inet_pton.c',
        'source/lib/ldap.c',
        'source/lib/llist.c',
        'source/lib/md4.c',
        'source/lib/md5.c',
        'source/lib/memdebug.c',
        'source/lib/mprintf.c',
        'source/lib/multi.c',
        'source/lib/netrc.c',
        'source/lib/non-ascii.c',
        'source/lib/nonblock.c',
        'source/lib/openldap.c',
        'source/lib/parsedate.c',
        'source/lib/pingpong.c',
        'source/lib/pipeline.c',
        'source/lib/pop3.c',
        'source/lib/progress.c',
        'source/lib/rawstr.c',
        'source/lib/rtsp.c',
        'source/lib/security.c',
        'source/lib/select.c',
        'source/lib/sendf.c',
        'source/lib/share.c',
        'source/lib/slist.c',
        'source/lib/smtp.c',
        'source/lib/socks.c',
        'source/lib/socks_gssapi.c',
        'source/lib/socks_sspi.c',
        'source/lib/speedcheck.c',
        'source/lib/splay.c',
        'source/lib/ssh.c',
        'source/lib/strdup.c',
        'source/lib/strequal.c',
        'source/lib/strerror.c',
        'source/lib/strtok.c',
        'source/lib/strtoofft.c',
        'source/lib/telnet.c',
        'source/lib/tftp.c',
        'source/lib/timeval.c',
        'source/lib/transfer.c',
        'source/lib/url.c',
        'source/lib/version.c',
        'source/lib/vtls/axtls.c',
        'source/lib/vtls/curl_darwinssl.c',
        'source/lib/vtls/curl_schannel.c',
        'source/lib/vtls/cyassl.c',
        'source/lib/vtls/gskit.c',
        'source/lib/vtls/gtls.c',
        'source/lib/vtls/nss.c',
        'source/lib/vtls/openssl.c',
        'source/lib/vtls/polarssl.c',
        'source/lib/vtls/polarssl_threadlock.c',
        'source/lib/vtls/qssl.c',
        'source/lib/vtls/vtls.c',
        'source/lib/warnless.c',
        'source/lib/wildcard.c',
      ],
    },
    {
      'target_name': 'curl',
      'type': 'executable',
      'include_dirs': [
        'source/lib',
        'source/src',
      ],
      'dependencies': [
        'curl_config',
        'libcurl',
      ],
      'sources': [
        'config/dummy_tool_hugehelp.c',
        'source/src/tool_binmode.c',
        'source/src/tool_bname.c',
        'source/src/tool_cb_dbg.c',
        'source/src/tool_cb_hdr.c',
        'source/src/tool_cb_prg.c',
        'source/src/tool_cb_rea.c',
        'source/src/tool_cb_see.c',
        'source/src/tool_cb_wrt.c',
        'source/src/tool_cfgable.c',
        'source/src/tool_convert.c',
        'source/src/tool_dirhie.c',
        'source/src/tool_doswin.c',
        'source/src/tool_easysrc.c',
        'source/src/tool_formparse.c',
        'source/src/tool_getparam.c',
        'source/src/tool_getpass.c',
        'source/src/tool_help.c',
        'source/src/tool_helpers.c',
        'source/src/tool_homedir.c',
        'source/src/tool_libinfo.c',
        'source/src/tool_main.c',
        'source/src/tool_metalink.c',
        'source/src/tool_mfiles.c',
        'source/src/tool_msgs.c',
        'source/src/tool_operate.c',
        'source/src/tool_operhlp.c',
        'source/src/tool_panykey.c',
        'source/src/tool_paramhlp.c',
        'source/src/tool_parsecfg.c',
        'source/src/tool_setopt.c',
        'source/src/tool_sleep.c',
        'source/src/tool_urlglob.c',
        'source/src/tool_util.c',
        'source/src/tool_vms.c',
        'source/src/tool_writeenv.c',
        'source/src/tool_writeout.c',
        'source/src/tool_xattr.c',
      ],
    },
  ],
}
