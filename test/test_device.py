from premonition.device import JuniperDevice
from premonition.configwriter import ConfigWriter
from premonition.lexer import Lexer


def test_lldp_configuration():
    configuration = """
    protocols {
        lldp {
            advertisement-interval 30;
            hold-multiplier 4;
            interface all {
                disable;
            }
            interface ge-1/1/1;
            interface xe-1/1/1 {
                tlv-filter system-name;
            }            
            lldp-configuration-notification-interval 30;
            ptopo-configuration-maximum-hold-time 300;
            ptopo-configuration-trap-interval 30;
            transmit-delay 2;
        }
    }    
    """


    dev = JuniperDevice(hostname="test-router", configuration=configuration)
    dev.build_models()
    
    assert dev.model.lldp.interfaces["all"].enabled is False
    assert dev.model.lldp.interfaces["ge-1/1/1"].enabled is True
    assert "tlv-filter system-name" in dev.model.lldp.interfaces["xe-1/1/1"].features 
    assert "ptopo-configuration-maximum-hold-time 300" in dev.model.lldp.features