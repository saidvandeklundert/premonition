from src.models.device import JuniperDevice
from src.juniper.configwriter import ConfigWriter
from src.juniper.lexer import Lexer
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
    lexer = Lexer(source=configuration)
    lexer.read_tokens()
    
    cb = ConfigWriter(tokens=lexer.tokens)
    configuration = cb.build_set_config()

    dev = JuniperDevice(hostname="test-router", configuration=configuration)
    dev.build_models()
    
    assert dev.lldp.interfaces["all"].enabled is False
    assert dev.lldp.interfaces["ge-1/1/1"].enabled is True
    assert "tlv-filter system-name" in dev.lldp.interfaces["xe-1/1/1"].features 
    assert "ptopo-configuration-maximum-hold-time 300" in dev.lldp.features