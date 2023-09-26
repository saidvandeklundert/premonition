# for every configuration file in test date, create a corresponding token file.
from juniper.configwriter import ConfigWriter
from juniper.lexer import Lexer
import glob
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
import json

original = """security {
    nat {        
        source {
            rule-set VENDOR_NAT {
                from zone VENDOR;
                to zone WAN;
                rule VENDOR_NO_NAT_DHCP {
                    match {
                        source-address 25.0.0.0/13;
                        destination-address [ 100.94.3.159/32 100.94.4.192/32 ];
                        destination-port {
                            67;
                        }
                    }
                    then {
                        source-nat {
                            off;
                        }
                    }
                }
            }
        }
    }
}
"""

converted = """
set security nat source rule-set VENDOR_NAT from zone VENDOR
set security nat source rule-set VENDOR_NAT to zone WAN
set security nat source rule-set VENDOR_NAT rule VENDOR_NO_NAT_DHCP match source-address 25.0.0.0/13
set security nat source rule-set VENDOR_NAT rule VENDOR_NO_NAT_DHCP match destination-address 100.94.3.159/32
set security nat source rule-set VENDOR_NAT rule VENDOR_NO_NAT_DHCP match destination-address 100.94.4.192/32
set security nat source rule-set VENDOR_NAT rule VENDOR_NO_NAT_DHCP match destination-port 67
set security nat source rule-set VENDOR_NAT rule VENDOR_NO_NAT_DHCP then source-nat off"""

lexer = Lexer(source=original)
lexer.read_tokens()
cb = ConfigWriter(tokens=lexer.tokens)
outcome = cb.build_set_config()
print(outcome)
print(converted)
# breakpoint()
print(bool(outcome.strip() == converted.strip()))
