from premonition.device import JuniperDevice
from premonition.configwriter import ConfigWriter
from premonition.lexer import Lexer


def test_juniper_lldp_builder():
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


def test_juniper_vlans_builder():
    configuration = """
    vlans {
        VLAN101 {
            vlan-id 101;
        }
        VLAN102 {
            vlan-id 102;
        }
        VLAN103 {
            vlan-id 103;
        }
        VLAN110 {
            vlan-id 110;
        }
        VLAN310 {                    
            vlan-id 310;
        }
        VLAN684 {
            vlan-id 684;
        }
        VLAN697 {
            vlan-id 697;
        }
        VLAN698 {
            vlan-id 698;
            l3-interface irb.698;
        }    
        VLAN699 {
            vlan-id 699;
        }
    }
    """
    dev = JuniperDevice(hostname="test-router", configuration=configuration)
    dev.build_models()

    assert dev.model.vlans[699].name == "VLAN699"
    assert dev.model.vlans[699].layer3_interface  is None
    assert dev.model.vlans[698].name == "VLAN698"
    assert dev.model.vlans[698].layer3_interface == "irb.698"