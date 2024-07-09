import gxutils
#
# auto-generated pixi build code file
# Build: G30_R7_0_0 | Yang: infinera
#

def create_card(handle, required_type, chassis_name, slot_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param required_type: Required card type.
    :type required_type: str
    :param chassis_name: Chassis where this card is located.
    :type chassis_name: unknown
    :param slot_name: Slot where this card is located.
    :type slot_name: str

    **Optional Parameters**:

        :card_name: str - Card identifier.
        :baud_rate: str - The configured baud-rate for this card's console port. Default value is card type specific.
        :local_switch: str - Defines the global access to all card's console port. Access can be overridden per console port at the card level.
        :port_name: str - Port name.
        :connected_to: str - Indicate neighbour port entity to which the current port is connected to. This is not validated by the NE and can be used by the customers (or NMS) for topology construction. This parameter is available independently on any automated discovery mechanisms that may exist in the port.
        :external_connectivity: str - Indicates whether the port is connected or to be connected externally or not.
        :port_alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :port_admin_state: str - The administrative state of the managed object.
        :port_alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :port_label: str - User label.
        :property_name: str - Name of the property.
        :value: str - Value of the property. Will always be a 'string', even if it corresponds to a number or other type.
        :required_subtype: str - The subtype of the card
        :card_mode: str - The configured card-mode, identifies specific card functionality.
        :subslot_name: str - Subslot where this card is located, e.g. 1-2.3 (slot 2, subslot 3). 'subslot-name' can only be set on (sub)card creation.
        :power_profile: str - User configured power draw for this card.
        :card_alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :card_admin_state: str - The administrative state of the managed object.
        :card_alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :card_label: str - User label.
    """

    card_name = kwargs.get('card_name', None)
    baud_rate = kwargs.get('baud_rate', None)
    local_switch = kwargs.get('local_switch', None)
    port_name = kwargs.get('port_name', None)
    connected_to = kwargs.get('connected_to', None)
    external_connectivity = kwargs.get('external_connectivity', None)
    port_alias_name = kwargs.get('port_alias_name', None)
    port_admin_state = kwargs.get('port_admin_state', None)
    port_alarm_report_control = kwargs.get('port_alarm_report_control', None)
    port_label = kwargs.get('port_label', None)
    property_name = kwargs.get('property_name', None)
    value = kwargs.get('value', None)
    required_subtype = kwargs.get('required_subtype', None)
    card_mode = kwargs.get('card_mode', None)
    subslot_name = kwargs.get('subslot_name', None)
    power_profile = kwargs.get('power_profile', None)
    card_alias_name = kwargs.get('card_alias_name', None)
    card_admin_state = kwargs.get('card_admin_state', None)
    card_alarm_report_control = kwargs.get('card_alarm_report_control', None)
    card_label = kwargs.get('card_label', None)

    object_name = 'Card'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "controller-card": {},
                        "console": {
                            "baud-rate": baud_rate,
                            "local-switch": local_switch
                        },
                        "port": [
                            {
                                "name": port_name,
                                "connected-to": connected_to,
                                "external-connectivity": external_connectivity,
                                "alias-name": port_alias_name,
                                "admin-state": port_admin_state,
                                "alarm-report-control": port_alarm_report_control,
                                "label": port_label
                            }
                        ],
                        "property": [
                            {
                                "name": property_name,
                                "value": value
                            }
                        ],
                        "required-type": required_type,
                        "required-subtype": required_subtype,
                        "card-mode": card_mode,
                        "chassis-name": chassis_name,
                        "slot-name": slot_name,
                        "subslot-name": subslot_name,
                        "power-profile": power_profile,
                        "alias-name": card_alias_name,
                        "admin-state": card_admin_state,
                        "alarm-report-control": card_alarm_report_control,
                        "label": card_label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_card(handle, card_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param card_name: Card identifier.
    :type card_name: str
    """

    object_name = 'Card'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_card(handle, card_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param required_type: Required card type.
    :type required_type: str
    :param chassis_name: Chassis where this card is located.
    :type chassis_name: unknown
    :param slot_name: Slot where this card is located.
    :type slot_name: str

    **Optional Parameters**:

        :card_name: str - Card identifier.
        :baud_rate: str - The configured baud-rate for this card's console port. Default value is card type specific.
        :local_switch: str - Defines the global access to all card's console port. Access can be overridden per console port at the card level.
        :port_name: str - Port name.
        :connected_to: str - Indicate neighbour port entity to which the current port is connected to. This is not validated by the NE and can be used by the customers (or NMS) for topology construction. This parameter is available independently on any automated discovery mechanisms that may exist in the port.
        :external_connectivity: str - Indicates whether the port is connected or to be connected externally or not.
        :port_alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :port_admin_state: str - The administrative state of the managed object.
        :port_alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :port_label: str - User label.
        :property_name: str - Name of the property.
        :value: str - Value of the property. Will always be a 'string', even if it corresponds to a number or other type.
        :required_subtype: str - The subtype of the card
        :card_mode: str - The configured card-mode, identifies specific card functionality.
        :subslot_name: str - Subslot where this card is located, e.g. 1-2.3 (slot 2, subslot 3). 'subslot-name' can only be set on (sub)card creation.
        :power_profile: str - User configured power draw for this card.
        :card_alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :card_admin_state: str - The administrative state of the managed object.
        :card_alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :card_label: str - User label.
    """

    baud_rate = kwargs.get('baud_rate', None)
    local_switch = kwargs.get('local_switch', None)
    connected_to = kwargs.get('connected_to', None)
    external_connectivity = kwargs.get('external_connectivity', None)
    port_alias_name = kwargs.get('port_alias_name', None)
    port_admin_state = kwargs.get('port_admin_state', None)
    port_alarm_report_control = kwargs.get('port_alarm_report_control', None)
    port_label = kwargs.get('port_label', None)
    value = kwargs.get('value', None)
    required_type = kwargs.get('required_type', None)
    required_subtype = kwargs.get('required_subtype', None)
    card_mode = kwargs.get('card_mode', None)
    chassis_name = kwargs.get('chassis_name', None)
    slot_name = kwargs.get('slot_name', None)
    subslot_name = kwargs.get('subslot_name', None)
    power_profile = kwargs.get('power_profile', None)
    card_alias_name = kwargs.get('card_alias_name', None)
    card_admin_state = kwargs.get('card_admin_state', None)
    card_alarm_report_control = kwargs.get('card_alarm_report_control', None)
    card_label = kwargs.get('card_label', None)

    object_name = 'Card'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "controller-card": {},
                        "console": {
                            "baud-rate": baud_rate,
                            "local-switch": local_switch
                        },
                        "port": [
                            {
                                "name": port_name,
                                "connected-to": connected_to,
                                "external-connectivity": external_connectivity,
                                "alias-name": port_alias_name,
                                "admin-state": port_admin_state,
                                "alarm-report-control": port_alarm_report_control,
                                "label": port_label
                            }
                        ],
                        "property": [
                            {
                                "name": property_name,
                                "value": value
                            }
                        ],
                        "required-type": required_type,
                        "required-subtype": required_subtype,
                        "card-mode": card_mode,
                        "chassis-name": chassis_name,
                        "slot-name": slot_name,
                        "subslot-name": subslot_name,
                        "power-profile": power_profile,
                        "alias-name": card_alias_name,
                        "admin-state": card_admin_state,
                        "alarm-report-control": card_alarm_report_control,
                        "label": card_label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def delete_card(handle, card_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param card_name: Card identifier.
    :type card_name: str
    """

    object_name = 'Card'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_port(handle, card_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param required_type: The type of the TOM.
    :type required_type: str

    **Optional Parameters**:

        :card_name: str - Card identifier.
        :port_name: str - Port name.
        :required_subtype: str - The subtype of the TOM.
        :phy_mode: str - Configured Phy Mode.
        :power_class_override: str - Used to override the power class for 3rd party TOM.
        :enable_serdes: bool - Controls enabling/disabling of configuring TOM SerDes.
        :tom_alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :tom_admin_state: str - The administrative state of the managed object.
        :tom_alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :tom_label: str - User label.
        :auto_negotiation: str - Auto negotiation mode.
        :mtu: int - The maximum transmission unit size in octets for the physical Ethernet port.
        :duplex_mode: str - Duplex mode; only valid if auto-negotiation is disabled.
        :rate: str - Required Ethernet rate; only valid if auto-negotiation is disabled.
        :flow_control: str - Specifies the type of flow control to be supported.
        :connected_to: str - Indicate neighbour port entity to which the current port is connected to. This is not validated by the NE and can be used by the customers (or NMS) for topology construction. This parameter is available independently on any automated discovery mechanisms that may exist in the port.
        :external_connectivity: str - Indicates whether the port is connected or to be connected externally or not.
        :port_alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :port_admin_state: str - The administrative state of the managed object.
        :port_alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :port_label: str - User label.
    """

    required_type = kwargs.get('required_type', None)
    required_subtype = kwargs.get('required_subtype', None)
    phy_mode = kwargs.get('phy_mode', None)
    power_class_override = kwargs.get('power_class_override', None)
    enable_serdes = kwargs.get('enable_serdes', None)
    tom_alias_name = kwargs.get('tom_alias_name', None)
    tom_admin_state = kwargs.get('tom_admin_state', None)
    tom_alarm_report_control = kwargs.get('tom_alarm_report_control', None)
    tom_label = kwargs.get('tom_label', None)
    auto_negotiation = kwargs.get('auto_negotiation', None)
    mtu = kwargs.get('mtu', None)
    duplex_mode = kwargs.get('duplex_mode', None)
    rate = kwargs.get('rate', None)
    flow_control = kwargs.get('flow_control', None)
    connected_to = kwargs.get('connected_to', None)
    external_connectivity = kwargs.get('external_connectivity', None)
    port_alias_name = kwargs.get('port_alias_name', None)
    port_admin_state = kwargs.get('port_admin_state', None)
    port_alarm_report_control = kwargs.get('port_alarm_report_control', None)
    port_label = kwargs.get('port_label', None)

    object_name = 'Port'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "port": [
                            {
                                "name": port_name,
                                "tom": {
                                    "required-type": required_type,
                                    "required-subtype": required_subtype,
                                    "phy-mode": phy_mode,
                                    "power-class-override": power_class_override,
                                    "enable-serdes": enable_serdes,
                                    "alias-name": tom_alias_name,
                                    "admin-state": tom_admin_state,
                                    "alarm-report-control": tom_alarm_report_control,
                                    "label": tom_label
                                },
                                "comm-eth": {
                                    "auto-negotiation": auto_negotiation,
                                    "mtu": mtu,
                                    "duplex-mode": duplex_mode,
                                    "rate": rate,
                                    "flow-control": flow_control
                                },
                                "connected-to": connected_to,
                                "external-connectivity": external_connectivity,
                                "alias-name": port_alias_name,
                                "admin-state": port_admin_state,
                                "alarm-report-control": port_alarm_report_control,
                                "label": port_label
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_port(handle, card_name, port_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param card_name: Card identifier.
    :type card_name: str
    :param port_name: Port name.
    :type port_name: str
    """

    object_name = 'Port'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "port": [
                            {
                                "name": port_name
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_tom(handle, required_type, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param required_type: The type of the TOM.
    :type required_type: str

    **Optional Parameters**:

        :card_name: str - Card identifier.
        :port_name: str - Port name.
        :serdes_name: str - Name of the advanced parameter.
        :value: str - Value of the advanced parameter.
        :required_subtype: str - The subtype of the TOM.
        :phy_mode: str - Configured Phy Mode.
        :power_class_override: str - Used to override the power class for 3rd party TOM.
        :enable_serdes: bool - Controls enabling/disabling of configuring TOM SerDes.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
    """

    card_name = kwargs.get('card_name', None)
    port_name = kwargs.get('port_name', None)
    serdes_name = kwargs.get('serdes_name', None)
    value = kwargs.get('value', None)
    required_subtype = kwargs.get('required_subtype', None)
    phy_mode = kwargs.get('phy_mode', None)
    power_class_override = kwargs.get('power_class_override', None)
    enable_serdes = kwargs.get('enable_serdes', None)
    alias_name = kwargs.get('alias_name', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)

    object_name = 'TOM'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "port": [
                            {
                                "name": port_name,
                                "tom": {
                                    "serdes": [
                                        {
                                            "name": serdes_name,
                                            "value": value
                                        }
                                    ],
                                    "required-type": required_type,
                                    "required-subtype": required_subtype,
                                    "phy-mode": phy_mode,
                                    "power-class-override": power_class_override,
                                    "enable-serdes": enable_serdes,
                                    "alias-name": alias_name,
                                    "admin-state": admin_state,
                                    "alarm-report-control": alarm_report_control,
                                    "label": label
                                }
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_tom(handle, card_name, port_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param card_name: Card identifier.
    :type card_name: str
    :param port_name: Port name.
    :type port_name: str
    """

    object_name = 'TOM'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "port": [
                            {
                                "name": port_name,
                                "tom": {}
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_tom(handle, card_name, port_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param card_name: Card identifier.
    :type card_name: str
    :param port_name: Port name.
    :type port_name: str
    """

    object_name = 'TOM'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "card": [
                    {
                        "name": card_name,
                        "port": [
                            {
                                "name": port_name,
                                "tom": {
                                    "@operation": "delete"
                                }
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_chassis(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param required_type: Chassis type.
    :type required_type: str

    **Optional Parameters**:

        :name: str - Chassis name.
        :expected_serial_number: str - Inform the NC the serial number of a sub-chassis. For the main-chassis, the value is auto-filled with its own serial number
        :required_subtype: str - The subtype of the chassis
        :chassis_location: str - User defined location
        :rack_name: str - User defined rack name (withing the location)
        :position_in_rack: int - Position of the chassis within the rack.
        :expected_pem_type: str - Defines what is the expected type of PEMs that this chassis will have. It is not possible to configure each PEM slot individually, as all PEMs need to be of the same type.
        :expected_fan_type: str - Defines what is the expected type of FANs that this chassis will have. It is not possible to configure each FAN slot individually, this needs to be done at the chassis level.
        :pem_under_voltage_threshold: str - Under voltage threshold on PEM input feed.
        :pem_over_voltage_threshold: str - Over voltage threshold on PEM input feed.
        :configured_max_power_draw: str - User configured limit of power usable by this chassis. If current-estimated-power-draw used in this chassis goes above the configured-max-power-draw, the alarm PWRDRAW is raised. 10000W represents a 'very high' power draw that is beyond any chassis possibilities, so having this value means this feature is disabled, and the alarm is never raised.
        :configured_ambient_temperature: int - Configured ambient temperature for the chassis, used to compute the FRU's power consumption.
        :power_redundancy: str - Configuration of the PEM redundancy mode.
        :no_switchover: str - If enabled, the standby controller will be locked out from taking over the active card. This means no manual or autonomous switchovers will happen.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
    """

    expected_serial_number = kwargs.get('expected_serial_number', None)
    required_type = kwargs.get('required_type', None)
    required_subtype = kwargs.get('required_subtype', None)
    chassis_location = kwargs.get('chassis_location', None)
    rack_name = kwargs.get('rack_name', None)
    position_in_rack = kwargs.get('position_in_rack', None)
    expected_pem_type = kwargs.get('expected_pem_type', None)
    expected_fan_type = kwargs.get('expected_fan_type', None)
    pem_under_voltage_threshold = kwargs.get('pem_under_voltage_threshold', None)
    pem_over_voltage_threshold = kwargs.get('pem_over_voltage_threshold', None)
    configured_max_power_draw = kwargs.get('configured_max_power_draw', None)
    configured_ambient_temperature = kwargs.get('configured_ambient_temperature', None)
    power_redundancy = kwargs.get('power_redundancy', None)
    no_switchover = kwargs.get('no_switchover', None)
    alias_name = kwargs.get('alias_name', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)

    object_name = 'Chassis'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "chassis": [
                    {
                        "name": name,
                        "expected-serial-number": expected_serial_number,
                        "required-type": required_type,
                        "required-subtype": required_subtype,
                        "chassis-location": chassis_location,
                        "rack-name": rack_name,
                        "position-in-rack": position_in_rack,
                        "expected-pem-type": expected_pem_type,
                        "expected-fan-type": expected_fan_type,
                        "pem-under-voltage-threshold": pem_under_voltage_threshold,
                        "pem-over-voltage-threshold": pem_over_voltage_threshold,
                        "configured-max-power-draw": configured_max_power_draw,
                        "configured-ambient-temperature": configured_ambient_temperature,
                        "power-redundancy": power_redundancy,
                        "no-switchover": no_switchover,
                        "alias-name": alias_name,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "label": label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_chassis(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Chassis name.
    :type name: str
    """

    object_name = 'Chassis'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "equipment": {
                "chassis": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_line_ptp(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :service_type: str - service-type to provison line side service.
        :line_system_mode: str - Indicates the specific mode of power control configured on the L1 transponder, and specifically, on this particular SCG port within the L1 transponder. The attribute indicates the L1 <-> L0 local power controls to adjust the Tx power from the L1 transponder towards the L0 line-system card (such as a WSS or Mux or Amplifier).
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :auto_in_service_enabled: bool - Auto-in-service switch for this facility.
        :valid_signal_time: int - Configurable time that represents a detection of a valid signal. Used for auto-in-service mechanism.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :power_threshold_low_offset: str - A user configurable attribute that results in the 'effective lower threshold' based on which the system raises the OPR-OORL alarm. The effective threshold will be (threshold-low + threshold-low-offset).
        :power_threshold_high_offset: str - A user configurable attribute that results in the 'effective upper threshold' based on which the system raises the OPR-OORH alarm. The effective threshold will be (threshold-high + threshold-high-offset).
    """

    service_type = kwargs.get('service_type', None)
    line_system_mode = kwargs.get('line_system_mode', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    auto_in_service_enabled = kwargs.get('auto_in_service_enabled', None)
    valid_signal_time = kwargs.get('valid_signal_time', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    power_threshold_low_offset = kwargs.get('power_threshold_low_offset', None)
    power_threshold_high_offset = kwargs.get('power_threshold_high_offset', None)

    object_name = 'Line-PTP'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "line-ptp": [
                    {
                        "name": name,
                        "service-type": service_type,
                        "line-system-mode": line_system_mode,
                        "label": label,
                        "admin-state": admin_state,
                        "auto-in-service-enabled": auto_in_service_enabled,
                        "valid-signal-time": valid_signal_time,
                        "alarm-report-control": alarm_report_control,
                        "power-threshold-low-offset": power_threshold_low_offset,
                        "power-threshold-high-offset": power_threshold_high_offset
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_line_ptp(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Line-PTP'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "line-ptp": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_flexo_group(handle, rate, modulation_format, group_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param rate: Carried signal basic rate class
    :type rate: str
    :param modulation_format: Current modulation format
    :type modulation_format: str
    :param group_id: 20bits, indicate the interface group instance that the FlexO-x interface is a member of. It will be unique in the NE
    :type group_id: int

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :fec_type: str - The FEC type
        :carriers: str - A list of carriers that are bound to this facilities. Possible values can be any card/resources/supported-carriers.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    name = kwargs.get('name', None)
    fec_type = kwargs.get('fec_type', None)
    carriers = kwargs.get('carriers', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'Flexo-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "flexo-group": [
                    {
                        "name": name,
                        "rate": rate,
                        "modulation-format": modulation_format,
                        "fec-type": fec_type,
                        "group-id": group_id,
                        "carriers": carriers,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_flexo_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Flexo-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "flexo-group": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_flexo_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Flexo-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "flexo-group": [
                    {
                        "name": name,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_ethernet(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :max_packet_length: int - Maximum transfer unit for ethernet facility, in octets.
        :fec_mode: str - The configured FEC mode on the Ethernet client. Default is dependent on configured client type.
        :tx_mapping_mode: str - The tx mapping mode of client port. The possible values are dependent on the HW and configuration.
        :expected_mapping_mode: str - The expected mapping mode of client port. The possible values are dependent on the HW and configuration.
        :time_slots: str - Time slots of the ethernet.
        :line_port: unknown - Specify the line port for the client. Can only be configured when mapping mode is openZR+.
        :fec_degraded_ser_monitoring: str - Allows to enable monitoring for FEC-DEGRADED-SER alarm.
        :fec_degraded_ser_activate_threshold: str - FEC-DEGRADED-SER alarm asserted if average SER, computed over accumulated FEC symbol errors in the monitoring period exceed this threshold.
        :fec_degraded_ser_deactivate_threshold: str - FEC-DEGRADED-SER alarm cleared if average SER, computed over accumulated FEC symbol errors in the monitoring period is below this threshold.
        :fec_degraded_ser_monitoring_period: int - Monitoring period duration over which FEC symbol errors are accumulated for asserting or clearing of FEC-DEGRADED-SER alarm.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :loopback: str - Loopback mode.Useful to debug on the fiber connection.
        :loopback_mode: str - Indicates loopback action for facility or terminal.
        :test_signal_type: str - The type of test pattern that is injected.
        :test_signal_direction: str - The direction of the test signal.
        :test_signal_monitoring: bool - Monitor the incoming test signals for diagnostics.
    """

    max_packet_length = kwargs.get('max_packet_length', None)
    fec_mode = kwargs.get('fec_mode', None)
    tx_mapping_mode = kwargs.get('tx_mapping_mode', None)
    expected_mapping_mode = kwargs.get('expected_mapping_mode', None)
    time_slots = kwargs.get('time_slots', None)
    line_port = kwargs.get('line_port', None)
    fec_degraded_ser_monitoring = kwargs.get('fec_degraded_ser_monitoring', None)
    fec_degraded_ser_activate_threshold = kwargs.get('fec_degraded_ser_activate_threshold', None)
    fec_degraded_ser_deactivate_threshold = kwargs.get('fec_degraded_ser_deactivate_threshold', None)
    fec_degraded_ser_monitoring_period = kwargs.get('fec_degraded_ser_monitoring_period', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    loopback = kwargs.get('loopback', None)
    loopback_mode = kwargs.get('loopback_mode', None)
    test_signal_type = kwargs.get('test_signal_type', None)
    test_signal_direction = kwargs.get('test_signal_direction', None)
    test_signal_monitoring = kwargs.get('test_signal_monitoring', None)

    object_name = 'Ethernet'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ethernet": [
                    {
                        "name": name,
                        "max-packet-length": max_packet_length,
                        "fec-mode": fec_mode,
                        "tx-mapping-mode": tx_mapping_mode,
                        "expected-mapping-mode": expected_mapping_mode,
                        "time-slots": time_slots,
                        "line-port": line_port,
                        "fec-degraded-ser-monitoring": fec_degraded_ser_monitoring,
                        "fec-degraded-ser-activate-threshold": fec_degraded_ser_activate_threshold,
                        "fec-degraded-ser-deactivate-threshold": fec_degraded_ser_deactivate_threshold,
                        "fec-degraded-ser-monitoring-period": fec_degraded_ser_monitoring_period,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "loopback": loopback,
                        "loopback-mode": loopback_mode,
                        "test-signal-type": test_signal_type,
                        "test-signal-direction": test_signal_direction,
                        "test-signal-monitoring": test_signal_monitoring
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_ethernet(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Ethernet'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ethernet": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_optical_carrier(handle, optical_carrier_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param value: Value of the advanced parameter.
    :type value: str

    **Optional Parameters**:

        :optical_carrier_name: str - A generic, configurable name for every facility.
        :advanced_parameter_name: str - Name of the advanced parameter.
        :frequency: str - The center frequency this carrier is tuned to. Zero means 'not configured'.
        :frequency_offset: int - A super set range for line and client side carrier, specific sub-range is depend on application. Frequency-offset can be used for bright tuning of the wavelengths. Once set, the frequency will slowly change (over 1-10s) without affecting service.
        :tx_power: str - The optical carrier's transmit power into the fiber from the transponder's optics. NOTE: The accuracy of the Tx Power can be adjusted in steps of 0.5 dBm.
        :pre_fec_q_sig_deg_threshold: str - The threshold based on which the PRE-FEC-Q-SIGNAL-DEGRADE alarm is raised. 0 implies threshold crossing alarming disabled. Specific sub-range is per carrier use-case.
        :pre_fec_q_sig_deg_hysteresis: str - Hysteresis to account for raising of the PRE-FEC-Q-SIGNAL-DEGRADE alarm.
        :enable_advanced_parameters: bool - Controls enabling/disabling of configuring advanced parameters for this object.
        :sop_data_collection: str - Controls enabling/disabling sop data collection, providing the collection interval in ms.     Only of relevance for carrier type ICE6.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :media_interface: str - Media interface type of ZR tom.
        :grid_spacing: str - Fixed Grid tunability for new 3rd party TOM.
        :tx_cd: str - The configured transmit pre-compensation chromatic dispersion.
        :post_fec_q_sig_deg_threshold: str - The threshold based on which the POST-FEC-Q-SIGNAL-DEGRADE alarm is raised.
        :post_fec_q_sig_deg_hysteresis: str - Hysteresis to account for raising of the POST-FEC-Q-SIGNAL-DEGRADE alarm.
        :rate: str - Carried signal basic rate class.
        :modulation_format: str - Current modulation format.
        :rx_frequency: str - The rx laser frequency. Special for 0 means it is same as tx laser frequency.
        :rx_attenuation: str - This is to support configurable optical attenuation at receiver side which is based on the hardware capability on the port.
        :tx_filter_roll_off: str - Transmitter filter roll off factor.
        :preemphasis: str - Preemphasis of transmitted signal.
        :preemphasis_value: str - Preemphasis of transmitted signal.
        :cd_range_low: int - Low value of chromatic dispersion search range.
        :cd_range_high: int - high value of chromatic dispersion search range.
        :cd_compensation_mode: str - chromatic dispersion compensation value source mode.
        :cd_compensation_value: int - manual chromatic dispersion compensation value
        :fast_sop_mode: str - Specify if enable fast SOP (state of polarization) change tracking; if enabled, the interface    will tolerate very fast SOP and transient.
        :BICHM: int - The BICHM (bit interleaved coded hybrid modulation) incremental step in 1/128 bits/symbol added to base modulation bits/symbol for the hybrid modes modulation-format. 0: Base modulation format bits/symbol; 1: 1/128 bits/symbol added to base modulation format bits/symbol; ... 127: 127/128 bits/symbol added to base modulation format bits/symbol
        :propagate_shutdown: str - When the attribute value is set to yes, the transmit laser will be shutdown if the whole service of the direction has signal failure, the function mainly used in regeneration node to propagate signal failure as LOS.
        :propagate_shutdown_holdoff_timer: int - The hold off time of propagate shutdown.
        :loopback: str - Loopback mode.Useful to debug on the fiber connection.
    """

    value = kwargs.get('value', None)
    frequency = kwargs.get('frequency', None)
    frequency_offset = kwargs.get('frequency_offset', None)
    tx_power = kwargs.get('tx_power', None)
    pre_fec_q_sig_deg_threshold = kwargs.get('pre_fec_q_sig_deg_threshold', None)
    pre_fec_q_sig_deg_hysteresis = kwargs.get('pre_fec_q_sig_deg_hysteresis', None)
    enable_advanced_parameters = kwargs.get('enable_advanced_parameters', None)
    sop_data_collection = kwargs.get('sop_data_collection', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    media_interface = kwargs.get('media_interface', None)
    grid_spacing = kwargs.get('grid_spacing', None)
    tx_cd = kwargs.get('tx_cd', None)
    post_fec_q_sig_deg_threshold = kwargs.get('post_fec_q_sig_deg_threshold', None)
    post_fec_q_sig_deg_hysteresis = kwargs.get('post_fec_q_sig_deg_hysteresis', None)
    rate = kwargs.get('rate', None)
    modulation_format = kwargs.get('modulation_format', None)
    rx_frequency = kwargs.get('rx_frequency', None)
    rx_attenuation = kwargs.get('rx_attenuation', None)
    tx_filter_roll_off = kwargs.get('tx_filter_roll_off', None)
    preemphasis = kwargs.get('preemphasis', None)
    preemphasis_value = kwargs.get('preemphasis_value', None)
    cd_range_low = kwargs.get('cd_range_low', None)
    cd_range_high = kwargs.get('cd_range_high', None)
    cd_compensation_mode = kwargs.get('cd_compensation_mode', None)
    cd_compensation_value = kwargs.get('cd_compensation_value', None)
    fast_sop_mode = kwargs.get('fast_sop_mode', None)
    BICHM = kwargs.get('BICHM', None)
    propagate_shutdown = kwargs.get('propagate_shutdown', None)
    propagate_shutdown_holdoff_timer = kwargs.get('propagate_shutdown_holdoff_timer', None)
    loopback = kwargs.get('loopback', None)

    object_name = 'Optical-Carrier'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "optical-carrier": [
                    {
                        "name": optical_carrier_name,
                        "advanced-parameter": [
                            {
                                "name": advanced_parameter_name,
                                "value": value
                            }
                        ],
                        "frequency": frequency,
                        "frequency-offset": frequency_offset,
                        "tx-power": tx_power,
                        "pre-fec-q-sig-deg-threshold": pre_fec_q_sig_deg_threshold,
                        "pre-fec-q-sig-deg-hysteresis": pre_fec_q_sig_deg_hysteresis,
                        "enable-advanced-parameters": enable_advanced_parameters,
                        "sop-data-collection": sop_data_collection,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "media-interface": media_interface,
                        "grid-spacing": grid_spacing,
                        "tx-cd": tx_cd,
                        "post-fec-q-sig-deg-threshold": post_fec_q_sig_deg_threshold,
                        "post-fec-q-sig-deg-hysteresis": post_fec_q_sig_deg_hysteresis,
                        "rate": rate,
                        "modulation-format": modulation_format,
                        "rx-frequency": rx_frequency,
                        "rx-attenuation": rx_attenuation,
                        "tx-filter-roll-off": tx_filter_roll_off,
                        "preemphasis": preemphasis,
                        "preemphasis-value": preemphasis_value,
                        "cd-range-low": cd_range_low,
                        "cd-range-high": cd_range_high,
                        "cd-compensation-mode": cd_compensation_mode,
                        "cd-compensation-value": cd_compensation_value,
                        "fast-sop-mode": fast_sop_mode,
                        "BICHM": BICHM,
                        "propagate-shutdown": propagate_shutdown,
                        "propagate-shutdown-holdoff-timer": propagate_shutdown_holdoff_timer,
                        "loopback": loopback
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_optical_carrier(handle, optical_carrier_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param optical_carrier_name: A generic, configurable name for every facility.
    :type optical_carrier_name: str
    """

    object_name = 'Optical-Carrier'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "optical-carrier": [
                    {
                        "name": optical_carrier_name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_odu(handle, odu_type, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param odu_type: The protocol type of the ODUk/ODUCn client.
    :type odu_type: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :direction: str - Diagnostics direction.Can be ingress or egress.
        :test_signal_monitoring_type: str - The type of test pattern that is monitored.
        :monitoring_mode: str - The monitoring mode on the ODU/OTU client.
        :tti_mismatch_alarm_reporting: str - Indicates if TTI-Mismatch (TIM) alarm is reported or not. If it is to be reported, indicates the criteria based on with the TIM alarm is reported.
        :tim_act_enabled: str - Support configurable TIM action which decide if insert maintenance signal per TIM: enable or disable, default disable
        :tti_style: str - The configured mode of the TTI for this OTU/ODU client or OTS.
        :tx_tti: str - Transmit TTI - Sent by this facility to the far-end remote facility.
        :expected_tti: str - Expected TTI - The TTI this facility expects to receive from the far-end remote facility.
        :expected_sapi: str - The expected SAPI (Source Access Point Identifier).
        :expected_dapi: str - The expected DAPI (Destination Access Point Identifier).
        :tx_sapi: str - The transmitted SAPI bytes.
        :tx_dapi: str - The transmitted DAPI bytes.
        :expected_operator: str - The expected operator specific bytes.
        :tx_operator: str - The transmitted operator specific bytes.
        :degrade_interval: int - The consecutive number of 1s intervals with the number of detected block errors exceeding the block error threshold for each of those seconds for the purposes of SDBER detection.
        :degrade_threshold: int - The threshold in percentage of block errors versus total blocks at which a degrade-interval number of seconds will be considered degraded for the purposes of SDBER detection.
        :test_signal_type: str - The type of test pattern that is injected.
        :test_signal_direction: str - The direction of the test signal.
        :test_signal_monitoring: bool - Monitor the incoming test signals for diagnostics.
        :parent_odu: unknown - For low order ODUs, points to the the parent HO-ODU name.
        :trib_port_number: int - Number of OPUk/OPUCn trib port that are part of this ODUk/ODUCn container.
        :instance_id: int - Optional parameter on LO-ODU creation, identifies the ODU within the parent/high-order ODU. If not provided, it is automatically derived. Max value depends on capacity of the HO-ODU and of the odu-type. (ex: for creating an ODU4 in a HO ODUC8, instance can be between 1 and 8)
        :tx_payload_type: str - Transmitter payload-type of ODU
        :delay_measurement_enable: str - The enable switching of delay-measurement function, when applicable.
        :msim_config: str - Specifies MSIM alarm reporting or not when msi value received not followed G.709 definition.
        :client_signal_type: str - Client signal type for ODUflex  CBR client. Applied to 200/400 GBE client on CHM1R and FC4/8/16 for UTM2 It is set automatically for the client side ODU, and need to be configured by the user at line side ODUj. Used for rate matching and bandwidth validation in the odu cross connection.
        :expected_payload_type: str - Expected payload-type of ODU
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :time_slots: str - Time slots of the ODU.
        :opucn_time_slots: str - Opucn Time slots of the ODUCn.
        :loopback: str - Loopback mode.Useful to debug on the fiber connection.
        :loopback_mode: str - Indicates loopback action for facility or terminal.
        :expected_trib_port_number: int - Expected Tributary Port Number for the LO-ODU entity.
        :expected_time_slots: str - Expected TS for the LO-ODU entity.
    """

    name = kwargs.get('name', None)
    direction = kwargs.get('direction', None)
    test_signal_monitoring_type = kwargs.get('test_signal_monitoring_type', None)
    monitoring_mode = kwargs.get('monitoring_mode', None)
    tti_mismatch_alarm_reporting = kwargs.get('tti_mismatch_alarm_reporting', None)
    tim_act_enabled = kwargs.get('tim_act_enabled', None)
    tti_style = kwargs.get('tti_style', None)
    tx_tti = kwargs.get('tx_tti', None)
    expected_tti = kwargs.get('expected_tti', None)
    expected_sapi = kwargs.get('expected_sapi', None)
    expected_dapi = kwargs.get('expected_dapi', None)
    tx_sapi = kwargs.get('tx_sapi', None)
    tx_dapi = kwargs.get('tx_dapi', None)
    expected_operator = kwargs.get('expected_operator', None)
    tx_operator = kwargs.get('tx_operator', None)
    degrade_interval = kwargs.get('degrade_interval', None)
    degrade_threshold = kwargs.get('degrade_threshold', None)
    test_signal_type = kwargs.get('test_signal_type', None)
    test_signal_direction = kwargs.get('test_signal_direction', None)
    test_signal_monitoring = kwargs.get('test_signal_monitoring', None)
    parent_odu = kwargs.get('parent_odu', None)
    trib_port_number = kwargs.get('trib_port_number', None)
    instance_id = kwargs.get('instance_id', None)
    tx_payload_type = kwargs.get('tx_payload_type', None)
    delay_measurement_enable = kwargs.get('delay_measurement_enable', None)
    msim_config = kwargs.get('msim_config', None)
    client_signal_type = kwargs.get('client_signal_type', None)
    expected_payload_type = kwargs.get('expected_payload_type', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    time_slots = kwargs.get('time_slots', None)
    opucn_time_slots = kwargs.get('opucn_time_slots', None)
    loopback = kwargs.get('loopback', None)
    loopback_mode = kwargs.get('loopback_mode', None)
    expected_trib_port_number = kwargs.get('expected_trib_port_number', None)
    expected_time_slots = kwargs.get('expected_time_slots', None)

    object_name = 'ODU'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "odu": [
                    {
                        "name": name,
                        "odu-diagnostics": [
                            {
                                "direction": direction,
                                "test-signal-monitoring-type": test_signal_monitoring_type,
                                "monitoring-mode": monitoring_mode,
                                "tti-mismatch-alarm-reporting": tti_mismatch_alarm_reporting,
                                "tim-act-enabled": tim_act_enabled,
                                "tti-style": tti_style,
                                "tx-tti": tx_tti,
                                "expected-tti": expected_tti,
                                "expected-sapi": expected_sapi,
                                "expected-dapi": expected_dapi,
                                "tx-sapi": tx_sapi,
                                "tx-dapi": tx_dapi,
                                "expected-operator": expected_operator,
                                "tx-operator": tx_operator,
                                "degrade-interval": degrade_interval,
                                "degrade-threshold": degrade_threshold,
                                "test-signal-type": test_signal_type,
                                "test-signal-direction": test_signal_direction,
                                "test-signal-monitoring": test_signal_monitoring
                            }
                        ],
                        "parent-odu": parent_odu,
                        "odu-type": odu_type,
                        "trib-port-number": trib_port_number,
                        "instance-id": instance_id,
                        "tx-payload-type": tx_payload_type,
                        "delay-measurement-enable": delay_measurement_enable,
                        "msim-config": msim_config,
                        "client-signal-type": client_signal_type,
                        "expected-payload-type": expected_payload_type,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "time-slots": time_slots,
                        "opucn-time-slots": opucn_time_slots,
                        "loopback": loopback,
                        "loopback-mode": loopback_mode,
                        "expected-trib-port-number": expected_trib_port_number,
                        "expected-time-slots": expected_time_slots
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_odu(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param odu_type: The protocol type of the ODUk/ODUCn client.
    :type odu_type: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :direction: str - Diagnostics direction.Can be ingress or egress.
        :test_signal_monitoring_type: str - The type of test pattern that is monitored.
        :monitoring_mode: str - The monitoring mode on the ODU/OTU client.
        :tti_mismatch_alarm_reporting: str - Indicates if TTI-Mismatch (TIM) alarm is reported or not. If it is to be reported, indicates the criteria based on with the TIM alarm is reported.
        :tim_act_enabled: str - Support configurable TIM action which decide if insert maintenance signal per TIM: enable or disable, default disable
        :tti_style: str - The configured mode of the TTI for this OTU/ODU client or OTS.
        :tx_tti: str - Transmit TTI - Sent by this facility to the far-end remote facility.
        :expected_tti: str - Expected TTI - The TTI this facility expects to receive from the far-end remote facility.
        :expected_sapi: str - The expected SAPI (Source Access Point Identifier).
        :expected_dapi: str - The expected DAPI (Destination Access Point Identifier).
        :tx_sapi: str - The transmitted SAPI bytes.
        :tx_dapi: str - The transmitted DAPI bytes.
        :expected_operator: str - The expected operator specific bytes.
        :tx_operator: str - The transmitted operator specific bytes.
        :degrade_interval: int - The consecutive number of 1s intervals with the number of detected block errors exceeding the block error threshold for each of those seconds for the purposes of SDBER detection.
        :degrade_threshold: int - The threshold in percentage of block errors versus total blocks at which a degrade-interval number of seconds will be considered degraded for the purposes of SDBER detection.
        :test_signal_type: str - The type of test pattern that is injected.
        :test_signal_direction: str - The direction of the test signal.
        :test_signal_monitoring: bool - Monitor the incoming test signals for diagnostics.
        :parent_odu: unknown - For low order ODUs, points to the the parent HO-ODU name.
        :trib_port_number: int - Number of OPUk/OPUCn trib port that are part of this ODUk/ODUCn container.
        :instance_id: int - Optional parameter on LO-ODU creation, identifies the ODU within the parent/high-order ODU. If not provided, it is automatically derived. Max value depends on capacity of the HO-ODU and of the odu-type. (ex: for creating an ODU4 in a HO ODUC8, instance can be between 1 and 8)
        :tx_payload_type: str - Transmitter payload-type of ODU
        :delay_measurement_enable: str - The enable switching of delay-measurement function, when applicable.
        :msim_config: str - Specifies MSIM alarm reporting or not when msi value received not followed G.709 definition.
        :client_signal_type: str - Client signal type for ODUflex  CBR client. Applied to 200/400 GBE client on CHM1R and FC4/8/16 for UTM2 It is set automatically for the client side ODU, and need to be configured by the user at line side ODUj. Used for rate matching and bandwidth validation in the odu cross connection.
        :expected_payload_type: str - Expected payload-type of ODU
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :time_slots: str - Time slots of the ODU.
        :opucn_time_slots: str - Opucn Time slots of the ODUCn.
        :loopback: str - Loopback mode.Useful to debug on the fiber connection.
        :loopback_mode: str - Indicates loopback action for facility or terminal.
        :expected_trib_port_number: int - Expected Tributary Port Number for the LO-ODU entity.
        :expected_time_slots: str - Expected TS for the LO-ODU entity.
    """

    test_signal_monitoring_type = kwargs.get('test_signal_monitoring_type', None)
    monitoring_mode = kwargs.get('monitoring_mode', None)
    tti_mismatch_alarm_reporting = kwargs.get('tti_mismatch_alarm_reporting', None)
    tim_act_enabled = kwargs.get('tim_act_enabled', None)
    tti_style = kwargs.get('tti_style', None)
    tx_tti = kwargs.get('tx_tti', None)
    expected_tti = kwargs.get('expected_tti', None)
    expected_sapi = kwargs.get('expected_sapi', None)
    expected_dapi = kwargs.get('expected_dapi', None)
    tx_sapi = kwargs.get('tx_sapi', None)
    tx_dapi = kwargs.get('tx_dapi', None)
    expected_operator = kwargs.get('expected_operator', None)
    tx_operator = kwargs.get('tx_operator', None)
    degrade_interval = kwargs.get('degrade_interval', None)
    degrade_threshold = kwargs.get('degrade_threshold', None)
    test_signal_type = kwargs.get('test_signal_type', None)
    test_signal_direction = kwargs.get('test_signal_direction', None)
    test_signal_monitoring = kwargs.get('test_signal_monitoring', None)
    parent_odu = kwargs.get('parent_odu', None)
    odu_type = kwargs.get('odu_type', None)
    trib_port_number = kwargs.get('trib_port_number', None)
    instance_id = kwargs.get('instance_id', None)
    tx_payload_type = kwargs.get('tx_payload_type', None)
    delay_measurement_enable = kwargs.get('delay_measurement_enable', None)
    msim_config = kwargs.get('msim_config', None)
    client_signal_type = kwargs.get('client_signal_type', None)
    expected_payload_type = kwargs.get('expected_payload_type', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    time_slots = kwargs.get('time_slots', None)
    opucn_time_slots = kwargs.get('opucn_time_slots', None)
    loopback = kwargs.get('loopback', None)
    loopback_mode = kwargs.get('loopback_mode', None)
    expected_trib_port_number = kwargs.get('expected_trib_port_number', None)
    expected_time_slots = kwargs.get('expected_time_slots', None)

    object_name = 'ODU'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "odu": [
                    {
                        "name": name,
                        "odu-diagnostics": [
                            {
                                "direction": direction,
                                "test-signal-monitoring-type": test_signal_monitoring_type,
                                "monitoring-mode": monitoring_mode,
                                "tti-mismatch-alarm-reporting": tti_mismatch_alarm_reporting,
                                "tim-act-enabled": tim_act_enabled,
                                "tti-style": tti_style,
                                "tx-tti": tx_tti,
                                "expected-tti": expected_tti,
                                "expected-sapi": expected_sapi,
                                "expected-dapi": expected_dapi,
                                "tx-sapi": tx_sapi,
                                "tx-dapi": tx_dapi,
                                "expected-operator": expected_operator,
                                "tx-operator": tx_operator,
                                "degrade-interval": degrade_interval,
                                "degrade-threshold": degrade_threshold,
                                "test-signal-type": test_signal_type,
                                "test-signal-direction": test_signal_direction,
                                "test-signal-monitoring": test_signal_monitoring
                            }
                        ],
                        "parent-odu": parent_odu,
                        "odu-type": odu_type,
                        "trib-port-number": trib_port_number,
                        "instance-id": instance_id,
                        "tx-payload-type": tx_payload_type,
                        "delay-measurement-enable": delay_measurement_enable,
                        "msim-config": msim_config,
                        "client-signal-type": client_signal_type,
                        "expected-payload-type": expected_payload_type,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "time-slots": time_slots,
                        "opucn-time-slots": opucn_time_slots,
                        "loopback": loopback,
                        "loopback-mode": loopback_mode,
                        "expected-trib-port-number": expected_trib_port_number,
                        "expected-time-slots": expected_time_slots
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_odu(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'ODU'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "odu": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_odu(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'ODU'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "odu": [
                    {
                        "name": name,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_xcon(handle, source, destination, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point between which the XCON needs to be created.
    :type source: str
    :param destination: The destination end-point between which the XCON needs to be created.
    :type destination: str

    **Optional Parameters**:

        :name: str - A user configured name for the XCON.
        :payload_type: str - Indicates a generic, high-level source (from) client payload type of the digital XCON.
        :direction: str - Indicates whether the digital XCON is uni-directional (1-WAY) or bi-directional (2-WAY).
        :circuit_id_suffix: str - User configured circuit ID suffix.
        :label: str - User label.
    """

    name = kwargs.get('name', None)
    payload_type = kwargs.get('payload_type', None)
    direction = kwargs.get('direction', None)
    circuit_id_suffix = kwargs.get('circuit_id_suffix', None)
    label = kwargs.get('label', None)

    object_name = 'XCON'
    manager = kwargs.get('manager')

    source = gxutils.get_fullpath_from_aid(source)
    destination = gxutils.get_fullpath_from_aid(source)

    request = {
        "ne": {
            "services": {
                "xcon": [
                    {
                        "name": name,
                        "source": source,
                        "destination": destination,
                        "payload-type": payload_type,
                        "direction": direction,
                        "circuit-id-suffix": circuit_id_suffix,
                        "label": label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_xcon(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A user configured name for the XCON.
    :type name: str
    """

    object_name = 'XCON'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "services": {
                "xcon": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_xcon(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A user configured name for the XCON.
    :type name: str
    """

    object_name = 'XCON'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "services": {
                "xcon": [
                    {
                        "name": name,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_ops(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :role: str - Allows the user to configure: - tributary: a single add/ drop to a local transponder, or to a remote transponder; local transponder: using port.external-connectivity = no; remote transponder: using port.external-connectivity = yes;  - multi-carrier: multiple-carriers on the underlying (filter) port; locally connected filter: using port.external-connectivity = no; remote (disaggregated) filter: using port.external-connectivity = yes;  - general-purpose: other cases: express cross-connection to another filter (created, or to be created.)
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    role = kwargs.get('role', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'OPS'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ops": [
                    {
                        "name": name,
                        "role": role,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_ops(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'OPS'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ops": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_ots(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :tti_style: str - The configured mode of the TTI for this OTU/ODU client or OTS.
        :nmoper_alarm_reporting: str - Indicates if a Neighbor Mismatch TTI Operator-Specific field based (NMOPER) alarm is reported or not.
        :expected_operator: str - The expected operator specific bytes.
        :tx_operator: str - The transmitted operator specific bytes.
        :osc_compatibility: str - Informs the system about the connected 7100 compatibility required.
        :osc_less: str - OSC-less mode is required to provide interworking with systems with no compatible OSC or spans with losses not compatible with the OSC budget.
        :fiber_type_rx: str - Fiber Type (OTS receiver) allows PCL to know the 'intercept' and 'slope'.
        :fiber_type_tx: str - Fiber Type (OTS transmitter) allows PCL to know the 'intercept' and 'slope'.
        :fiber_length_tx: str - Transmitting Fiber Length
        :fiber_length_rx: str - Receiving Fiber Length.
        :fiber_spectral_attenuation_tilt_tx: str - Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz.
        :fiber_spectral_attenuation_tilt_rx: str - Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz.
        :raman_coefficient_tx: str - Raman coefficient per Terahertz. Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz. Required for tilt control (if tilt-control-mode = auto). Configuration mode depends on tilt-control-mode.
        :raman_coefficient_rx: str - Raman coefficient per Terahertz. Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz. Required for tilt control (if tilt-control-mode = auto). Configuration mode depends on tilt-control-mode.
        :span_loss_reference: str - Configures span-loss source intended to be used by the system to calculate automatic target powers.
        :span_loss_receive: str - Fiber loss on the receiver side. (OTS-sk) This is only the loss of the fiber.
        :external_attenuation_tx: str - External padding attenuation at transmitting direction. Required for tilt control.
        :span_loss_aging_margin_rx: str - Used by system for defining value of span loss high alarm.
        :target_power_setting: str - Allows automatic configuration of target values for oxcon.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :span_loss_transmit: str - Fiber loss on the transmitter side (OTS-so). This is only the loss of the fiber. Additional loss such as coming from patch panel is entered via the external-attenuation parameters.
        :external_attenuation_rx: str - External Attenuation, configured by the user.
    """

    tti_style = kwargs.get('tti_style', None)
    nmoper_alarm_reporting = kwargs.get('nmoper_alarm_reporting', None)
    expected_operator = kwargs.get('expected_operator', None)
    tx_operator = kwargs.get('tx_operator', None)
    osc_compatibility = kwargs.get('osc_compatibility', None)
    osc_less = kwargs.get('osc_less', None)
    fiber_type_rx = kwargs.get('fiber_type_rx', None)
    fiber_type_tx = kwargs.get('fiber_type_tx', None)
    fiber_length_tx = kwargs.get('fiber_length_tx', None)
    fiber_length_rx = kwargs.get('fiber_length_rx', None)
    fiber_spectral_attenuation_tilt_tx = kwargs.get('fiber_spectral_attenuation_tilt_tx', None)
    fiber_spectral_attenuation_tilt_rx = kwargs.get('fiber_spectral_attenuation_tilt_rx', None)
    raman_coefficient_tx = kwargs.get('raman_coefficient_tx', None)
    raman_coefficient_rx = kwargs.get('raman_coefficient_rx', None)
    span_loss_reference = kwargs.get('span_loss_reference', None)
    span_loss_receive = kwargs.get('span_loss_receive', None)
    external_attenuation_tx = kwargs.get('external_attenuation_tx', None)
    span_loss_aging_margin_rx = kwargs.get('span_loss_aging_margin_rx', None)
    target_power_setting = kwargs.get('target_power_setting', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    span_loss_transmit = kwargs.get('span_loss_transmit', None)
    external_attenuation_rx = kwargs.get('external_attenuation_rx', None)

    object_name = 'OTS'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ots": [
                    {
                        "name": name,
                        "ots-diagnostics": {
                            "tti-style": tti_style,
                            "nmoper-alarm-reporting": nmoper_alarm_reporting,
                            "expected-operator": expected_operator,
                            "tx-operator": tx_operator
                        },
                        "osc-compatibility": osc_compatibility,
                        "osc-less": osc_less,
                        "fiber-type-rx": fiber_type_rx,
                        "fiber-type-tx": fiber_type_tx,
                        "fiber-length-tx": fiber_length_tx,
                        "fiber-length-rx": fiber_length_rx,
                        "fiber-spectral-attenuation-tilt-tx": fiber_spectral_attenuation_tilt_tx,
                        "fiber-spectral-attenuation-tilt-rx": fiber_spectral_attenuation_tilt_rx,
                        "raman-coefficient-tx": raman_coefficient_tx,
                        "raman-coefficient-rx": raman_coefficient_rx,
                        "span-loss-reference": span_loss_reference,
                        "span-loss-receive": span_loss_receive,
                        "external-attenuation-tx": external_attenuation_tx,
                        "span-loss-aging-margin-rx": span_loss_aging_margin_rx,
                        "target-power-setting": target_power_setting,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "span-loss-transmit": span_loss_transmit,
                        "external-attenuation-rx": external_attenuation_rx
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_ots(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'OTS'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ots": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_ots_r(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :required_fiber_type_rx: str - The required Fiber Type on the DWDM Line, with reference for the Rx fiber. Only of relevance if control-mode = auto. And: when there is no fiber-connection.
        :fiber_length_rx: str - Receiving Fiber Length
        :span_loss_receive: str - The Span Loss at the receiving dwdm-line.
        :delta_pointloss: str - Delta Pointloss (Rx) Additional attenuation that can be determined after turning up pumps. This is the fiber contribution for the pointloss: to be fine tuned in the field. This additional optical attenuation may be due to e.g. bad splice at dwdm-line Rx, higher att. than 0.1 dB.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :external_attenuation_rx: str - External Attenuation, configured by the user.
        :span_loss_transmit: str - Fiber loss on the transmitter side (OTS-so). This is only the loss of the fiber. Additional loss such as coming from patch panel is entered via the external-attenuation parameters.
    """

    required_fiber_type_rx = kwargs.get('required_fiber_type_rx', None)
    fiber_length_rx = kwargs.get('fiber_length_rx', None)
    span_loss_receive = kwargs.get('span_loss_receive', None)
    delta_pointloss = kwargs.get('delta_pointloss', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    external_attenuation_rx = kwargs.get('external_attenuation_rx', None)
    span_loss_transmit = kwargs.get('span_loss_transmit', None)

    object_name = 'OTS-R'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ots-r": [
                    {
                        "name": name,
                        "required-fiber-type-rx": required_fiber_type_rx,
                        "fiber-length-rx": fiber_length_rx,
                        "span-loss-receive": span_loss_receive,
                        "delta-pointloss": delta_pointloss,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "external-attenuation-rx": external_attenuation_rx,
                        "span-loss-transmit": span_loss_transmit
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_ots_r(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'OTS-R'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "ots-r": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_mc(handle, parent_oms, lower_frequency, upper_frequency, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param parent_oms: Parent Media Channel. Only set by creation. The referenced supporting-card must be part of a Degree (cannot be in an ADG).
    :type parent_oms: unknown
    :param lower_frequency: Lower Frequency of a Media Channel.
    :type lower_frequency: int
    :param upper_frequency: Upper Frequency of a Media Channel.
    :type upper_frequency: int

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    name = kwargs.get('name', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'MC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "mc": [
                    {
                        "name": name,
                        "parent-oms": parent_oms,
                        "lower-frequency": lower_frequency,
                        "upper-frequency": upper_frequency,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_mc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'MC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "mc": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_mc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'MC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "mc": [
                    {
                        "name": name,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_nmc(handle, parent_facility, center_frequency, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param parent_facility: Parent facility: can be either a Media Channel or an OMS. Only set on creation.
    :type parent_facility: str
    :param center_frequency: Nominal Center Frequency of the NMC
    :type center_frequency: int

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :width: int - Network Media Channel frequency width; unit is MHz. The value in GHz should be equivalent to the baud rate (GBd) configured on the connected transponder line interface line port.
        :input_power_min: str - Minimum Input Power.
        :input_power_max: str - Maximum Input Power.
        :input_power_typical: str - Typical Input Power.
        :input_power_min_offset: str - Minimum Input Power offset, of relevance for NMCs within MCs.
        :input_attenuation_target: str - Configurable target input attentuation.
        :output_attenuation_target: str - Configurable target output attentuation.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    name = kwargs.get('name', None)
    width = kwargs.get('width', None)
    input_power_min = kwargs.get('input_power_min', None)
    input_power_max = kwargs.get('input_power_max', None)
    input_power_typical = kwargs.get('input_power_typical', None)
    input_power_min_offset = kwargs.get('input_power_min_offset', None)
    input_attenuation_target = kwargs.get('input_attenuation_target', None)
    output_attenuation_target = kwargs.get('output_attenuation_target', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'NMC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "nmc": [
                    {
                        "name": name,
                        "parent-facility": parent_facility,
                        "center-frequency": center_frequency,
                        "width": width,
                        "input-power-min": input_power_min,
                        "input-power-max": input_power_max,
                        "input-power-typical": input_power_typical,
                        "input-power-min-offset": input_power_min_offset,
                        "input-attenuation-target": input_attenuation_target,
                        "output-attenuation-target": output_attenuation_target,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_nmc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'NMC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "nmc": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_nmc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'NMC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "nmc": [
                    {
                        "name": name,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_oxcon(handle, source, destination, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point required for OXcon creation.
    :type source: str
    :param destination: The destination end-point required for OXcon creation.
    :type destination: str

    **Optional Parameters**:

        :name: str - A user configured name for the OXcon.
        :direction: str - Set-by-create OXcon type.
        :target_output_power_src: str - The source interface target power.     Only of relevance for power working mode and two-way OXcon.
        :target_output_power_dst: str - The destination interface target power.     Only of relevance when connecting regular NMC.
        :circuit_id: str - Path/ service name of optical cross-connection.
        :label: str - User label.
    """

    name = kwargs.get('name', None)
    direction = kwargs.get('direction', None)
    target_output_power_src = kwargs.get('target_output_power_src', None)
    target_output_power_dst = kwargs.get('target_output_power_dst', None)
    circuit_id = kwargs.get('circuit_id', None)
    label = kwargs.get('label', None)

    object_name = 'OXCON'
    manager = kwargs.get('manager')

    source = /ioa-ne:ne/ioa-ne:facilities/ioa-ne:nmc[ioa-ne:name='{source}']
    destination = /ioa-ne:ne/ioa-ne:facilities/ioa-ne:nmc[ioa-ne:name='{destination}']

    request = {
        "ne": {
            "services": {
                "oxcon": [
                    {
                        "name": name,
                        "source": source,
                        "destination": destination,
                        "direction": direction,
                        "target-output-power-src": target_output_power_src,
                        "target-output-power-dst": target_output_power_dst,
                        "circuit-id": circuit_id,
                        "label": label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_oxcon(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A user configured name for the OXcon.
    :type name: str
    """

    object_name = 'OXCON'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "services": {
                "oxcon": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_oxcon(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A user configured name for the OXcon.
    :type name: str
    """

    object_name = 'OXCON'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "services": {
                "oxcon": [
                    {
                        "name": name,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_amplifier(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - Non-configurable name: derived from chass/slot and degree.
        :amplifier_enable: str - The enable switch of the amplifier.
        :control_mode: str - Type of control-mode.
        :gain_range_control: str - Automatic or Manual Gain Range configuration.
        :span_loss_control: str - Span Loss Control configuration.     Only of relevance for inline amplifier(s) and preamp(s).
        :gain_range_target: str - Gain Range Target
        :gain_target: str - For manual control mode: setting gain to the amplifier for constant-gain mode.
        :gain_adjustment: str - Gain range adjustment: For auto control mode: gain offset defined by the user. The value is used for adjustment of gain when the amplifier is in automatic control mode, the automatically calculated gain will include offset of this attribute. Only supported on amplifiers with 'function' = 'pa' or 'inline'.
        :output_voa_attenuation: str - For control-mode = 'manual': target VOA attenuation at output of the amplifier (line padding VOA).
        :tilt_control_mode: str - Specify the tilt control mode. Defines whether amplifier tilt is automatically set by system or configured manually by the user
        :tilt_target: str - For manual control mode: target tilt, to be configured on the amplifier.
        :tilt_adjustment: str - Used to offset the target tilt when tilt-control-mode = 'auto' / 'auto-planned'
        :raman_signal_gain: str - Raman Gain of C-Band (signal) - if there is a fiber-connection from/to Raman, the API raman-signal-gain at amplifier needs to be appropriately configured autonomously; - if there is no fiber-connection from/to Raman, user reads out the amplifier-raman.raman-signal-gain and should configure it on the amplifier.
        :raman_osc_gain: str - Raman Gain OSC (see raman-signal-gain).
        :admin_state: str - The administrative state of the managed object.
        :label: str - User label.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    amplifier_enable = kwargs.get('amplifier_enable', None)
    control_mode = kwargs.get('control_mode', None)
    gain_range_control = kwargs.get('gain_range_control', None)
    span_loss_control = kwargs.get('span_loss_control', None)
    gain_range_target = kwargs.get('gain_range_target', None)
    gain_target = kwargs.get('gain_target', None)
    gain_adjustment = kwargs.get('gain_adjustment', None)
    output_voa_attenuation = kwargs.get('output_voa_attenuation', None)
    tilt_control_mode = kwargs.get('tilt_control_mode', None)
    tilt_target = kwargs.get('tilt_target', None)
    tilt_adjustment = kwargs.get('tilt_adjustment', None)
    raman_signal_gain = kwargs.get('raman_signal_gain', None)
    raman_osc_gain = kwargs.get('raman_osc_gain', None)
    admin_state = kwargs.get('admin_state', None)
    label = kwargs.get('label', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'Amplifier'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "amplifier": [
                    {
                        "name": name,
                        "amplifier-enable": amplifier_enable,
                        "control-mode": control_mode,
                        "gain-range-control": gain_range_control,
                        "span-loss-control": span_loss_control,
                        "gain-range-target": gain_range_target,
                        "gain-target": gain_target,
                        "gain-adjustment": gain_adjustment,
                        "output-voa-attenuation": output_voa_attenuation,
                        "tilt-control-mode": tilt_control_mode,
                        "tilt-target": tilt_target,
                        "tilt-adjustment": tilt_adjustment,
                        "raman-signal-gain": raman_signal_gain,
                        "raman-osc-gain": raman_osc_gain,
                        "admin-state": admin_state,
                        "label": label,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_amplifier(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Non-configurable name: derived from chass/slot and degree.
    :type name: str
    """

    object_name = 'Amplifier'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "amplifier": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_degree(handle, supported_card, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param supported_card: Instance of card or subcard that belongs to degree.
    :type supported_card: str

    **Optional Parameters**:

        :degree_number: int - Degree number should be greater than zero and not greater than max-degrees.
        :index: int - Card with index 1 should be the card/ subcard/ module with DWDM line interface. Card with index 2 is only applicable to BAXOFP2, when card-mode = 'degree'. Index 2 cannot be used for PAx nor RD cards.
        :label: str - User label.
    """

    degree_number = kwargs.get('degree_number', None)
    index = kwargs.get('index', None)
    label = kwargs.get('label', None)

    object_name = 'Degree'
    manager = kwargs.get('manager')

    supported_card = /ioa-ne:ne/ioa-ne:equipment/ioa-ne:card[ioa-ne:name='{supported_card}']

    request = {
        "ne": {
            "ne-function": {
                "degree": [
                    {
                        "degree-number": degree_number,
                        "modules-degree": [
                            {
                                "index": index,
                                "supported-card": supported_card
                            }
                        ],
                        "label": label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_degree(handle, degree_number, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param supported_card: Instance of card or subcard that belongs to degree.
    :type supported_card: str

    **Optional Parameters**:

        :degree_number: int - Degree number should be greater than zero and not greater than max-degrees.
        :index: int - Card with index 1 should be the card/ subcard/ module with DWDM line interface. Card with index 2 is only applicable to BAXOFP2, when card-mode = 'degree'. Index 2 cannot be used for PAx nor RD cards.
        :label: str - User label.
    """

    supported_card = kwargs.get('supported_card', None)
    label = kwargs.get('label', None)

    object_name = 'Degree'
    manager = kwargs.get('manager')

    supported_card = /ioa-ne:ne/ioa-ne:equipment/ioa-ne:card[ioa-ne:name='{supported_card}']

    request = {
        "ne": {
            "ne-function": {
                "degree": [
                    {
                        "degree-number": degree_number,
                        "modules-degree": [
                            {
                                "index": index,
                                "supported-card": supported_card
                            }
                        ],
                        "label": label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_degree(handle, degree_number, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param degree_number: Degree number should be greater than zero and not greater than max-degrees.
    :type degree_number: int
    """

    object_name = 'Degree'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "degree": [
                    {
                        "degree-number": degree_number
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_degree(handle, degree_number, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param degree_number: Degree number should be greater than zero and not greater than max-degrees.
    :type degree_number: int
    """

    object_name = 'Degree'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "degree": [
                    {
                        "degree-number": degree_number,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_oc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :tx_mapping_mode: str - The tx mapping mode of client port. The possible values are dependent on the HW and configuration.
        :expected_mapping_mode: str - The expected mapping mode of client port. The possible values are dependent on the HW and configuration.
        :tti_style: str - The configured mode of the TTI.
        :tim_monitor: str - The enable switching of tim defect monitor mode.
        :tx_tti: str - Transmit TTI - Sent by this facility to the far-end remote facility.
        :expected_tti: str - Expected TTI - The TTI this facility expects to receive from the far-end remote facility.
        :loopback: str - Loopback mode.Useful to debug on the fiber connection.
        :loopback_mode: str - Indicates loopback action for facility or terminal.
        :test_signal_type: str - The type of test pattern that is injected.
        :test_signal_direction: str - The direction of the test signal.
        :test_signal_monitoring: bool - Monitor the incoming test signals for diagnostics.
    """

    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    tx_mapping_mode = kwargs.get('tx_mapping_mode', None)
    expected_mapping_mode = kwargs.get('expected_mapping_mode', None)
    tti_style = kwargs.get('tti_style', None)
    tim_monitor = kwargs.get('tim_monitor', None)
    tx_tti = kwargs.get('tx_tti', None)
    expected_tti = kwargs.get('expected_tti', None)
    loopback = kwargs.get('loopback', None)
    loopback_mode = kwargs.get('loopback_mode', None)
    test_signal_type = kwargs.get('test_signal_type', None)
    test_signal_direction = kwargs.get('test_signal_direction', None)
    test_signal_monitoring = kwargs.get('test_signal_monitoring', None)

    object_name = 'OC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "oc": [
                    {
                        "name": name,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "tx-mapping-mode": tx_mapping_mode,
                        "expected-mapping-mode": expected_mapping_mode,
                        "tti-style": tti_style,
                        "tim-monitor": tim_monitor,
                        "tx-tti": tx_tti,
                        "expected-tti": expected_tti,
                        "loopback": loopback,
                        "loopback-mode": loopback_mode,
                        "test-signal-type": test_signal_type,
                        "test-signal-direction": test_signal_direction,
                        "test-signal-monitoring": test_signal_monitoring
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_oc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'OC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "oc": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_fc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :tx_mapping_mode: str - The tx mapping mode of client port. The possible values are dependent on the HW and configuration.
        :expected_mapping_mode: str - The expected mapping mode of client port. The possible values are dependent on the HW and configuration.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :loopback: str - Loopback mode.Useful to debug on the fiber connection.
        :loopback_mode: str - Indicates loopback action for facility or terminal.
        :test_signal_type: str - The type of test pattern that is injected.
        :test_signal_direction: str - The direction of the test signal.
        :test_signal_monitoring: bool - Monitor the incoming test signals for diagnostics.
    """

    tx_mapping_mode = kwargs.get('tx_mapping_mode', None)
    expected_mapping_mode = kwargs.get('expected_mapping_mode', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    loopback = kwargs.get('loopback', None)
    loopback_mode = kwargs.get('loopback_mode', None)
    test_signal_type = kwargs.get('test_signal_type', None)
    test_signal_direction = kwargs.get('test_signal_direction', None)
    test_signal_monitoring = kwargs.get('test_signal_monitoring', None)

    object_name = 'FC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "fc": [
                    {
                        "name": name,
                        "tx-mapping-mode": tx_mapping_mode,
                        "expected-mapping-mode": expected_mapping_mode,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "loopback": loopback,
                        "loopback-mode": loopback_mode,
                        "test-signal-type": test_signal_type,
                        "test-signal-direction": test_signal_direction,
                        "test-signal-monitoring": test_signal_monitoring
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_fc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'FC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "fc": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_rib(handle, rib_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param rib_name: The name of the RIB.
    :type rib_name: str

    **Optional Parameters**:

        :destination_prefix: str - IP destination prefix.
        :vrf: unknown - VRF to which this RIB is bound.
        :address_family: str - Address family.
    """

    destination_prefix = kwargs.get('destination_prefix', None)
    vrf = kwargs.get('vrf', None)
    address_family = kwargs.get('address_family', None)

    object_name = 'RIB'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "rib": [
                        {
                            "rib-name": rib_name,
                            "route": [
                                {
                                    "destination-prefix": destination_prefix
                                }
                            ],
                            "vrf": vrf,
                            "address-family": address_family
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_rib(handle, rib_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param rib_name: The name of the RIB.
    :type rib_name: str

    **Optional Parameters**:

        :destination_prefix: str - IP destination prefix.
        :vrf: unknown - VRF to which this RIB is bound.
        :address_family: str - Address family.
    """

    vrf = kwargs.get('vrf', None)
    address_family = kwargs.get('address_family', None)

    object_name = 'RIB'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "rib": [
                        {
                            "rib-name": rib_name,
                            "route": [
                                {
                                    "destination-prefix": destination_prefix
                                }
                            ],
                            "vrf": vrf,
                            "address-family": address_family
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_rib(handle, rib_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param rib_name: The name of the RIB.
    :type rib_name: str
    """

    object_name = 'RIB'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "rib": [
                        {
                            "rib-name": rib_name
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_rib(handle, rib_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param rib_name: The name of the RIB.
    :type rib_name: str
    """

    object_name = 'RIB'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "rib": [
                        {
                            "rib-name": rib_name,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_adg(handle, supported_card, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param supported_card: Instance of the card for the ADG.
    :type supported_card: str

    **Optional Parameters**:

        :adg_number: int - ADG identifier as a number.
        :index: int - Card with index 1 should be the card/ subcard/ module fibered to the Degree(s).
        :ocm_monitoring: bool - 'true' if monitoring is provided by the Degree, or CD-AD structure; 'false' otherwise.
        :label: str - User label.
    """

    adg_number = kwargs.get('adg_number', None)
    index = kwargs.get('index', None)
    ocm_monitoring = kwargs.get('ocm_monitoring', None)
    label = kwargs.get('label', None)

    object_name = 'ADG'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "adg": [
                    {
                        "adg-number": adg_number,
                        "modules-adg": [
                            {
                                "index": index,
                                "supported-card": supported_card,
                                "ocm-monitoring": ocm_monitoring
                            }
                        ],
                        "label": label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_adg(handle, adg_number, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param supported_card: Instance of the card for the ADG.
    :type supported_card: str

    **Optional Parameters**:

        :adg_number: int - ADG identifier as a number.
        :index: int - Card with index 1 should be the card/ subcard/ module fibered to the Degree(s).
        :ocm_monitoring: bool - 'true' if monitoring is provided by the Degree, or CD-AD structure; 'false' otherwise.
        :label: str - User label.
    """

    supported_card = kwargs.get('supported_card', None)
    ocm_monitoring = kwargs.get('ocm_monitoring', None)
    label = kwargs.get('label', None)

    object_name = 'ADG'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "adg": [
                    {
                        "adg-number": adg_number,
                        "modules-adg": [
                            {
                                "index": index,
                                "supported-card": supported_card,
                                "ocm-monitoring": ocm_monitoring
                            }
                        ],
                        "label": label
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_adg(handle, adg_number, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param adg_number: ADG identifier as a number.
    :type adg_number: int
    """

    object_name = 'ADG'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "adg": [
                    {
                        "adg-number": adg_number
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_adg(handle, adg_number, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param adg_number: ADG identifier as a number.
    :type adg_number: int
    """

    object_name = 'ADG'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "adg": [
                    {
                        "adg-number": adg_number,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_amplifier_raman(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - Non-configurable name: derived from chass/slot and degree.
        :pump_id: int - 'pump-id' is an integer identifying the number of the pump.
        :target_pump_power: str - Raman Pump Power required.
        :control_mode: str - Control Mode for this Raman Amplifier.
        :amplifier_enable: str - Enable switch for this Raman. User configuration of Local Raman, and optionally control remote Raman card.
        :connected_amp_edfa_optimum_gain: str - Connected EDFA Optimum Gain; 0 means no known optimum gain, in case of disaggregated Raman.
        :target_raman_gain: str - Target Raman Gain, configurable in case control-mode = manual. In case control-mode = auto, this is then ignored.
        :admin_state: str - The administrative state of the managed object.
        :label: str - User label.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    target_pump_power = kwargs.get('target_pump_power', None)
    control_mode = kwargs.get('control_mode', None)
    amplifier_enable = kwargs.get('amplifier_enable', None)
    connected_amp_edfa_optimum_gain = kwargs.get('connected_amp_edfa_optimum_gain', None)
    target_raman_gain = kwargs.get('target_raman_gain', None)
    admin_state = kwargs.get('admin_state', None)
    label = kwargs.get('label', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'Amplifier-Raman'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "amplifier-raman": [
                    {
                        "name": name,
                        "pump-power": [
                            {
                                "pump-id": pump_id,
                                "target-pump-power": target_pump_power
                            }
                        ],
                        "control-mode": control_mode,
                        "amplifier-enable": amplifier_enable,
                        "connected-amp-edfa-optimum-gain": connected_amp_edfa_optimum_gain,
                        "target-raman-gain": target_raman_gain,
                        "admin-state": admin_state,
                        "label": label,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_amplifier_raman(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Non-configurable name: derived from chass/slot and degree.
    :type name: str
    """

    object_name = 'Amplifier-Raman'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "ne-function": {
                "amplifier-raman": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_comm_channel(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: Indicates the type of control channel.
    :type type: str
    :param parent: Parent object of the comm-channel.     Only of relevance when type is GCC0 or GCC1.
    :type parent: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :mtu: int - The maximum transmission unit size in octets for comm channel.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    type = kwargs.get('type', None)
    mtu = kwargs.get('mtu', None)
    parent = kwargs.get('parent', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'Comm-Channel'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "comm-channel": [
                    {
                        "name": name,
                        "type": type,
                        "mtu": mtu,
                        "parent": parent,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_comm_channel(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Comm-Channel'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "comm-channel": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_aaa_server(handle, server_priority, protocol_supported, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_priority: This is used to sort the servers in the order of precedence.
    :type server_priority: int
    :param protocol_supported: specify the protocol used for AAA.
    :type protocol_supported: str
    :param server_address: The IP address of AAA server.
    :type server_address: str

    **Optional Parameters**:

        :server_name: str - specify the name of aaa server.
        :server_port: str - AAA server port number.     Ony of relevance for protocol supported TACACSPLUS.
        :server_port_authentication: str - AAA server authentication port number.     Ony of relevance for protocol supported RADIUS.
        :server_port_accounting: str - AAA server accounting port number.     Ony of relevance for protocol supported RADIUS.
        :shared_secret: str - The shared secret of the aaa server. The shared secret will be displayed as *.
        :role_supported: str - The configured roles for the AAA server.
        :enabled: bool - Enable switch for this aaa-server.
        :timeout: int - Specifies the response timeout of Access-Request messages sent to a AAA server in seconds.
        :retry: int - Specifies the number of attempted Access-Request messages to a single AAA server before failing authentication.
        :source_ip: str - Source IP address used for RADIUS communications.     Only of relevance for protocol supported RADIUS.
        :common_password: str - Password used for RADIUS authorization after SSH public key authentication. If blank, username is reused as password for RADIUS authorization. Only of relevance for protocol supported RADIUS.
        :auth_protocol: str - The list of supported authentication protocols to use; if more than one is selected, system will try one at a time in a best-effort way. Authentication will be considered unsuccessful if none of the protocols work. Only of relevance for protocol supported TACACSPLUS.
    """

    server_name = kwargs.get('server_name', None)
    server_port = kwargs.get('server_port', None)
    server_port_authentication = kwargs.get('server_port_authentication', None)
    server_port_accounting = kwargs.get('server_port_accounting', None)
    shared_secret = kwargs.get('shared_secret', None)
    role_supported = kwargs.get('role_supported', None)
    enabled = kwargs.get('enabled', None)
    timeout = kwargs.get('timeout', None)
    retry = kwargs.get('retry', None)
    source_ip = kwargs.get('source_ip', None)
    common_password = kwargs.get('common_password', None)
    auth_protocol = kwargs.get('auth_protocol', None)

    object_name = 'AAA-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "aaa-server": [
                        {
                            "server-name": server_name,
                            "server-priority": server_priority,
                            "protocol-supported": protocol_supported,
                            "server-address": server_address,
                            "server-port": server_port,
                            "server-port-authentication": server_port_authentication,
                            "server-port-accounting": server_port_accounting,
                            "shared-secret": shared_secret,
                            "role-supported": role_supported,
                            "enabled": enabled,
                            "timeout": timeout,
                            "retry": retry,
                            "source-ip": source_ip,
                            "common-password": common_password,
                            "auth-protocol": auth_protocol
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_aaa_server(handle, server_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_priority: This is used to sort the servers in the order of precedence.
    :type server_priority: int
    :param protocol_supported: specify the protocol used for AAA.
    :type protocol_supported: str
    :param server_address: The IP address of AAA server.
    :type server_address: str

    **Optional Parameters**:

        :server_name: str - specify the name of aaa server.
        :server_port: str - AAA server port number.     Ony of relevance for protocol supported TACACSPLUS.
        :server_port_authentication: str - AAA server authentication port number.     Ony of relevance for protocol supported RADIUS.
        :server_port_accounting: str - AAA server accounting port number.     Ony of relevance for protocol supported RADIUS.
        :shared_secret: str - The shared secret of the aaa server. The shared secret will be displayed as *.
        :role_supported: str - The configured roles for the AAA server.
        :enabled: bool - Enable switch for this aaa-server.
        :timeout: int - Specifies the response timeout of Access-Request messages sent to a AAA server in seconds.
        :retry: int - Specifies the number of attempted Access-Request messages to a single AAA server before failing authentication.
        :source_ip: str - Source IP address used for RADIUS communications.     Only of relevance for protocol supported RADIUS.
        :common_password: str - Password used for RADIUS authorization after SSH public key authentication. If blank, username is reused as password for RADIUS authorization. Only of relevance for protocol supported RADIUS.
        :auth_protocol: str - The list of supported authentication protocols to use; if more than one is selected, system will try one at a time in a best-effort way. Authentication will be considered unsuccessful if none of the protocols work. Only of relevance for protocol supported TACACSPLUS.
    """

    server_priority = kwargs.get('server_priority', None)
    protocol_supported = kwargs.get('protocol_supported', None)
    server_address = kwargs.get('server_address', None)
    server_port = kwargs.get('server_port', None)
    server_port_authentication = kwargs.get('server_port_authentication', None)
    server_port_accounting = kwargs.get('server_port_accounting', None)
    shared_secret = kwargs.get('shared_secret', None)
    role_supported = kwargs.get('role_supported', None)
    enabled = kwargs.get('enabled', None)
    timeout = kwargs.get('timeout', None)
    retry = kwargs.get('retry', None)
    source_ip = kwargs.get('source_ip', None)
    common_password = kwargs.get('common_password', None)
    auth_protocol = kwargs.get('auth_protocol', None)

    object_name = 'AAA-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "aaa-server": [
                        {
                            "server-name": server_name,
                            "server-priority": server_priority,
                            "protocol-supported": protocol_supported,
                            "server-address": server_address,
                            "server-port": server_port,
                            "server-port-authentication": server_port_authentication,
                            "server-port-accounting": server_port_accounting,
                            "shared-secret": shared_secret,
                            "role-supported": role_supported,
                            "enabled": enabled,
                            "timeout": timeout,
                            "retry": retry,
                            "source-ip": source_ip,
                            "common-password": common_password,
                            "auth-protocol": auth_protocol
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_aaa_server(handle, server_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_name: specify the name of aaa server.
    :type server_name: str
    """

    object_name = 'AAA-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "aaa-server": [
                        {
                            "server-name": server_name
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_aaa_server(handle, server_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_name: specify the name of aaa server.
    :type server_name: str
    """

    object_name = 'AAA-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "aaa-server": [
                        {
                            "server-name": server_name,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_acl(handle, type, interface, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: Indicates the top-level type of ACL, i.e., what fields from the associated IPv4 or IPv6 headers this ACL matches on.
    :type type: str
    :param interface: A reference to the interface this filter shall be applied to.
    :type interface: unknown

    **Optional Parameters**:

        :name: str - Name of the ACL.
        :sequence_id: int - Sequence number that establishes the relative order of the ACE within an ACL
        :direction: str - Based on the direction, this filter shall be applied to incoming packets, or outgoing packets. Note that Input is mandatory and output is an optional function.
        :logging_action: bool - Flag to indicate if logging needs to be done once the ACE rule is matched.
        :source_ip_address: str - Specifies the source IP of this filter. The values could be a valid IPv4/v6-address or Ipv4/v6-address/prefix.
        :source_lower_port: str - The lower bound on the source Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :source_upper_port: str - The upper bound on the source Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :destination_ip_address: str - Specifies the destination IP of this filter. The values could be a valid IPv4/v6-address or Ipv4/v6-address/prefix.
        :destination_lower_port: str - The lower bound on the destination Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :destination_upper_port: str - The upper bound on the destination Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :ttl: str - IPv4 and IPv6 packet's time-to-live (TTL) hop limit. Default TTL value 255 is max hop
        :action: str - The action to be taken by the filter.
        :protocol: str - Internet Protocol number.  Refers to the protocol payload.  In IPv6, this field is known as 'next-header', and if extension headers are present, the protocol is present in the 'upper-layer' header.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
    """

    name = kwargs.get('name', None)
    sequence_id = kwargs.get('sequence_id', None)
    direction = kwargs.get('direction', None)
    logging_action = kwargs.get('logging_action', None)
    source_ip_address = kwargs.get('source_ip_address', None)
    source_lower_port = kwargs.get('source_lower_port', None)
    source_upper_port = kwargs.get('source_upper_port', None)
    destination_ip_address = kwargs.get('destination_ip_address', None)
    destination_lower_port = kwargs.get('destination_lower_port', None)
    destination_upper_port = kwargs.get('destination_upper_port', None)
    ttl = kwargs.get('ttl', None)
    action = kwargs.get('action', None)
    protocol = kwargs.get('protocol', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)

    object_name = 'ACL'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "access-control-list": {
                        "acl": [
                            {
                                "name": name,
                                "ace": [
                                    {
                                        "sequence-id": sequence_id,
                                        "direction": direction,
                                        "logging-action": logging_action,
                                        "source-ip-address": source_ip_address,
                                        "source-lower-port": source_lower_port,
                                        "source-upper-port": source_upper_port,
                                        "destination-ip-address": destination_ip_address,
                                        "destination-lower-port": destination_lower_port,
                                        "destination-upper-port": destination_upper_port,
                                        "ttl": ttl,
                                        "action": action,
                                        "protocol": protocol,
                                        "label": label
                                    }
                                ],
                                "type": type,
                                "interface": interface,
                                "admin-state": admin_state
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_acl(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: Indicates the top-level type of ACL, i.e., what fields from the associated IPv4 or IPv6 headers this ACL matches on.
    :type type: str
    :param interface: A reference to the interface this filter shall be applied to.
    :type interface: unknown

    **Optional Parameters**:

        :name: str - Name of the ACL.
        :sequence_id: int - Sequence number that establishes the relative order of the ACE within an ACL
        :direction: str - Based on the direction, this filter shall be applied to incoming packets, or outgoing packets. Note that Input is mandatory and output is an optional function.
        :logging_action: bool - Flag to indicate if logging needs to be done once the ACE rule is matched.
        :source_ip_address: str - Specifies the source IP of this filter. The values could be a valid IPv4/v6-address or Ipv4/v6-address/prefix.
        :source_lower_port: str - The lower bound on the source Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :source_upper_port: str - The upper bound on the source Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :destination_ip_address: str - Specifies the destination IP of this filter. The values could be a valid IPv4/v6-address or Ipv4/v6-address/prefix.
        :destination_lower_port: str - The lower bound on the destination Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :destination_upper_port: str - The upper bound on the destination Layer 4 TCP/UDP port number. A value of zero for both indicates wildcarding.
        :ttl: str - IPv4 and IPv6 packet's time-to-live (TTL) hop limit. Default TTL value 255 is max hop
        :action: str - The action to be taken by the filter.
        :protocol: str - Internet Protocol number.  Refers to the protocol payload.  In IPv6, this field is known as 'next-header', and if extension headers are present, the protocol is present in the 'upper-layer' header.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
    """

    direction = kwargs.get('direction', None)
    logging_action = kwargs.get('logging_action', None)
    source_ip_address = kwargs.get('source_ip_address', None)
    source_lower_port = kwargs.get('source_lower_port', None)
    source_upper_port = kwargs.get('source_upper_port', None)
    destination_ip_address = kwargs.get('destination_ip_address', None)
    destination_lower_port = kwargs.get('destination_lower_port', None)
    destination_upper_port = kwargs.get('destination_upper_port', None)
    ttl = kwargs.get('ttl', None)
    action = kwargs.get('action', None)
    protocol = kwargs.get('protocol', None)
    label = kwargs.get('label', None)
    type = kwargs.get('type', None)
    interface = kwargs.get('interface', None)
    admin_state = kwargs.get('admin_state', None)

    object_name = 'ACL'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "access-control-list": {
                        "acl": [
                            {
                                "name": name,
                                "ace": [
                                    {
                                        "sequence-id": sequence_id,
                                        "direction": direction,
                                        "logging-action": logging_action,
                                        "source-ip-address": source_ip_address,
                                        "source-lower-port": source_lower_port,
                                        "source-upper-port": source_upper_port,
                                        "destination-ip-address": destination_ip_address,
                                        "destination-lower-port": destination_lower_port,
                                        "destination-upper-port": destination_upper_port,
                                        "ttl": ttl,
                                        "action": action,
                                        "protocol": protocol,
                                        "label": label
                                    }
                                ],
                                "type": type,
                                "interface": interface,
                                "admin-state": admin_state
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_acl(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Name of the ACL.
    :type name: str
    """

    object_name = 'ACL'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "access-control-list": {
                        "acl": [
                            {
                                "name": name
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_acl(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Name of the ACL.
    :type name: str
    """

    object_name = 'ACL'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "networking": {
                    "access-control-list": {
                        "acl": [
                            {
                                "name": name,
                                "@operation": "delete"
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_dial_out_server(handle, address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param address: Dial-out-server IPv4/IPv6 address or hostname.
    :type address: str

    **Optional Parameters**:

        :name: str - Dial-out-server name.
        :protocol: str - Dial-out-server session type.
        :port: int - Dial-out-server session port.
        :retry_policy: str - Retry policy after a timeout.
        :retry: int - Number of retries before giving up.
        :timeout: int - Wait time until timeout.
        :auto_connect: bool - If true, automatically tries to connect to this dial-out-server. Note that a server with auto-connect false can still be connected manually via the call-home RPC.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
    """

    name = kwargs.get('name', None)
    protocol = kwargs.get('protocol', None)
    port = kwargs.get('port', None)
    retry_policy = kwargs.get('retry_policy', None)
    retry = kwargs.get('retry', None)
    timeout = kwargs.get('timeout', None)
    auto_connect = kwargs.get('auto_connect', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)

    object_name = 'Dial-Out-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "dial-out-server": [
                        {
                            "name": name,
                            "address": address,
                            "protocol": protocol,
                            "port": port,
                            "retry-policy": retry_policy,
                            "retry": retry,
                            "timeout": timeout,
                            "auto-connect": auto_connect,
                            "alarm-report-control": alarm_report_control,
                            "label": label
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_dial_out_server(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param address: Dial-out-server IPv4/IPv6 address or hostname.
    :type address: str

    **Optional Parameters**:

        :name: str - Dial-out-server name.
        :protocol: str - Dial-out-server session type.
        :port: int - Dial-out-server session port.
        :retry_policy: str - Retry policy after a timeout.
        :retry: int - Number of retries before giving up.
        :timeout: int - Wait time until timeout.
        :auto_connect: bool - If true, automatically tries to connect to this dial-out-server. Note that a server with auto-connect false can still be connected manually via the call-home RPC.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
    """

    address = kwargs.get('address', None)
    protocol = kwargs.get('protocol', None)
    port = kwargs.get('port', None)
    retry_policy = kwargs.get('retry_policy', None)
    retry = kwargs.get('retry', None)
    timeout = kwargs.get('timeout', None)
    auto_connect = kwargs.get('auto_connect', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)

    object_name = 'Dial-Out-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "dial-out-server": [
                        {
                            "name": name,
                            "address": address,
                            "protocol": protocol,
                            "port": port,
                            "retry-policy": retry_policy,
                            "retry": retry,
                            "timeout": timeout,
                            "auto-connect": auto_connect,
                            "alarm-report-control": alarm_report_control,
                            "label": label
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_dial_out_server(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Dial-out-server name.
    :type name: str
    """

    object_name = 'Dial-Out-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "dial-out-server": [
                        {
                            "name": name
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_dial_out_server(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Dial-out-server name.
    :type name: str
    """

    object_name = 'Dial-Out-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "dial-out-server": [
                        {
                            "name": name,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_ntp_key(handle, key_type, key_value, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param key_type: Hash algorithm for NTP message digest computation
    :type key_type: str
    :param key_value: NTP Key-value.
    :type key_value: str

    **Optional Parameters**:

        :key_id: int - NTP Key-ID.
        :is_trusted: bool - Is trusted NTP key.
    """

    key_id = kwargs.get('key_id', None)
    is_trusted = kwargs.get('is_trusted', None)

    object_name = 'NTP-Key'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-key": [
                        {
                            "key-id": key_id,
                            "key-type": key_type,
                            "key-value": key_value,
                            "is-trusted": is_trusted
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_ntp_key(handle, key_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param key_id: NTP Key-ID.
    :type key_id: int
    """

    object_name = 'NTP-Key'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-key": [
                        {
                            "key-id": key_id
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_ntp_key(handle, key_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param key_id: NTP Key-ID.
    :type key_id: int
    """

    object_name = 'NTP-Key'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-key": [
                        {
                            "key-id": key_id,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_ntp_server(handle, ip_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param ip_address: NTP Server IP address. Ipv4/Ipv6/hostname supported.
    :type ip_address: str

    **Optional Parameters**:

        :origin: str - NTP address assignment method, user can convert DHCP configured NTP entry into a manual configured by changing this attribute.
        :auth_key_id: str - Key ID to be used for this server.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    origin = kwargs.get('origin', None)
    auth_key_id = kwargs.get('auth_key_id', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'NTP-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-server": [
                        {
                            "ip-address": ip_address,
                            "origin": origin,
                            "auth-key-id": auth_key_id,
                            "label": label,
                            "admin-state": admin_state,
                            "alarm-report-control": alarm_report_control
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_ntp_server(handle, ip_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param ip_address: NTP Server IP address. Ipv4/Ipv6/hostname supported.
    :type ip_address: str

    **Optional Parameters**:

        :origin: str - NTP address assignment method, user can convert DHCP configured NTP entry into a manual configured by changing this attribute.
        :auth_key_id: str - Key ID to be used for this server.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    origin = kwargs.get('origin', None)
    auth_key_id = kwargs.get('auth_key_id', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'NTP-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-server": [
                        {
                            "ip-address": ip_address,
                            "origin": origin,
                            "auth-key-id": auth_key_id,
                            "label": label,
                            "admin-state": admin_state,
                            "alarm-report-control": alarm_report_control
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_ntp_server(handle, ip_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param ip_address: NTP Server IP address. Ipv4/Ipv6/hostname supported.
    :type ip_address: str
    """

    object_name = 'NTP-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-server": [
                        {
                            "ip-address": ip_address
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_ntp_server(handle, ip_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param ip_address: NTP Server IP address. Ipv4/Ipv6/hostname supported.
    :type ip_address: str
    """

    object_name = 'NTP-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-server": [
                        {
                            "ip-address": ip_address,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_ntp(handle, key_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param key_type: Hash algorithm for NTP message digest computation
    :type key_type: str
    :param key_value: NTP Key-value.
    :type key_value: str

    **Optional Parameters**:

        :key_id: int - NTP Key-ID.
        :is_trusted: bool - Is trusted NTP key.
        :ip_address: str - NTP Server IP address. Ipv4/Ipv6/hostname supported.
        :origin: str - NTP address assignment method, user can convert DHCP configured NTP entry into a manual configured by changing this attribute.
        :auth_key_id: str - Key ID to be used for this server.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :ntp_enabled: bool - Whether ntp is enabled.
        :ntp_auth_enabled: bool - Whether NTP authentication is enabled.
        :assignment_method: str - The system would contain manual and dhcp configured values. System can use those onfigurations/values defined by assignment-method attributes.
    """

    key_type = kwargs.get('key_type', None)
    key_value = kwargs.get('key_value', None)
    is_trusted = kwargs.get('is_trusted', None)
    origin = kwargs.get('origin', None)
    auth_key_id = kwargs.get('auth_key_id', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    ntp_enabled = kwargs.get('ntp_enabled', None)
    ntp_auth_enabled = kwargs.get('ntp_auth_enabled', None)
    assignment_method = kwargs.get('assignment_method', None)

    object_name = 'NTP'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {
                    "ntp-key": [
                        {
                            "key-id": key_id,
                            "key-type": key_type,
                            "key-value": key_value,
                            "is-trusted": is_trusted
                        }
                    ],
                    "ntp-server": [
                        {
                            "ip-address": ip_address,
                            "origin": origin,
                            "auth-key-id": auth_key_id,
                            "label": label,
                            "admin-state": admin_state,
                            "alarm-report-control": alarm_report_control
                        }
                    ],
                    "ntp-enabled": ntp_enabled,
                    "ntp-auth-enabled": ntp_auth_enabled,
                    "assignment-method": assignment_method
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_ntp(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'NTP'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "ntp": {}
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_netconf_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :enabled: bool - Enables/disables the NETCONF management protocol.
        :port: int - The port which listens for NETCONF access via ssh.
        :annotate_cli_name: bool - If enabled, annotates NETCONF XML output with cli names for traceability.
        :hello_timeout: int - Specifies the number of seconds that a session may exist before the hello PDU is received/transmitted.  A session will be dropped if no hello PDU is received/transmitted before this number of seconds elapses.
        :static_info_in_notifs: str - List of YANG identifiers that are statically included in notifications. If they are present in objects that are notified. Applicable for management protocols with support for YANG-type notifications (NETCONF, etc). For example, if object user[user-name='tom'] has had the 'timeout' attribute updated, and the static-info-in-notifs included the 'user-status' string, the associated notification would include not only the 'timeout' parameter, but also the 'user-status' (despite the fact that it had not changed).
    """

    enabled = kwargs.get('enabled', None)
    port = kwargs.get('port', None)
    annotate_cli_name = kwargs.get('annotate_cli_name', None)
    hello_timeout = kwargs.get('hello_timeout', None)
    static_info_in_notifs = kwargs.get('static_info_in_notifs', None)

    object_name = 'Netconf-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "netconf": {
                        "enabled": enabled,
                        "port": port,
                        "annotate-cli-name": annotate_cli_name,
                        "hello-timeout": hello_timeout,
                        "static-info-in-notifs": static_info_in_notifs
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_netconf_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'Netconf-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "netconf": {}
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_restconf_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :enabled: bool - User configurable switch to enable or disable RESTCONF access.
        :http_enabled: bool - User configurable switch to enable or disable RESTCONF HTTP access.
        :https_enabled: bool - User configurable switch to enable or disable RESTCONF HTTPS access.
        :http_port: int - User configurable RESTCONF HTTP port.
        :https_port: int - User configurable RESTCONF HTTPS port.
        :cookie_timeout: int - Timeout of a cookie based RESTCONF session.
    """

    enabled = kwargs.get('enabled', None)
    http_enabled = kwargs.get('http_enabled', None)
    https_enabled = kwargs.get('https_enabled', None)
    http_port = kwargs.get('http_port', None)
    https_port = kwargs.get('https_port', None)
    cookie_timeout = kwargs.get('cookie_timeout', None)

    object_name = 'Restconf-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "restconf": {
                        "enabled": enabled,
                        "http-enabled": http_enabled,
                        "https-enabled": https_enabled,
                        "http-port": http_port,
                        "https-port": https_port,
                        "cookie-timeout": cookie_timeout
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_restconf_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'Restconf-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "restconf": {}
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_grpc_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :enabled: bool - Enables/disables the gRPC management protocol.
        :port: int - The port which listens for gNMI & gNOI access via gRPC.
        :gnmi_get_encoding_granularity: str - Allows to configure the granularity of data in gNMI Get responses, when encoded with JSON.
    """

    enabled = kwargs.get('enabled', None)
    port = kwargs.get('port', None)
    gnmi_get_encoding_granularity = kwargs.get('gnmi_get_encoding_granularity', None)

    object_name = 'GRPC-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "grpc": {
                        "enabled": enabled,
                        "port": port,
                        "gnmi-get-encoding-granularity": gnmi_get_encoding_granularity
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_grpc_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'GRPC-Server'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "protocols": {
                    "grpc": {}
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def create_user(handle, user_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_name: The name of the user.
    :type user_name: str

    **Optional Parameters**:

        :password: str - The password of the user.
        :password_hashed: str - Hashed password of the user. It is made of three mandatory fields, where the dollar sign is the field separator. The structure is: $id$salt$encrypted Only id 6 (SHA512) is supported. Salt minimum size is 2. reference: https://www.man7.org/linux/man-pages/man3/crypt.3.html
        :display_name: str - The display name for this user.
        :max_invalid_login: int - This attribute is the maximum number of consecutive and invalid login attempts before an account is suspended (lockedout). Zero disables escalation on login failure.
        :suspension_time: int - This attribute is the duration of UID suspension following consecutive invalid login attempts. Setting the value to 0 disables this behavior.
        :timeout: int - This attribute is the Session Time Out Interval. If there are no messages between the user and the NE over the Time Out interval, the session is logged off. Setting the value to 0 disables this attribute (meaning the session will not time out).
        :password_aging_interval: int - This attribute is the Password Aging Interval. Setting the value to 0 disables password aging.
        :enabled: bool - Enable switch for the user, allows admins to explicitly disable users.
        :force_password_change: bool - Allows administrator to force user to change password on next login.
        :max_sessions: int - This attribute specifies the maximum number of sessions allowed for this user.
        :user_group: unknown - Associated user groups for this user.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
    """

    password = kwargs.get('password', None)
    password_hashed = kwargs.get('password_hashed', None)
    display_name = kwargs.get('display_name', None)
    max_invalid_login = kwargs.get('max_invalid_login', None)
    suspension_time = kwargs.get('suspension_time', None)
    timeout = kwargs.get('timeout', None)
    password_aging_interval = kwargs.get('password_aging_interval', None)
    enabled = kwargs.get('enabled', None)
    force_password_change = kwargs.get('force_password_change', None)
    max_sessions = kwargs.get('max_sessions', None)
    user_group = kwargs.get('user_group', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user": [
                        {
                            "user-name": user_name,
                            "password": password,
                            "password-hashed": password_hashed,
                            "display-name": display_name,
                            "max-invalid-login": max_invalid_login,
                            "suspension-time": suspension_time,
                            "timeout": timeout,
                            "password-aging-interval": password_aging_interval,
                            "enabled": enabled,
                            "force-password-change": force_password_change,
                            "max-sessions": max_sessions,
                            "user-group": user_group,
                            "alarm-report-control": alarm_report_control,
                            "label": label
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_user(handle, user_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_name: The name of the user.
    :type user_name: str

    **Optional Parameters**:

        :password: str - The password of the user.
        :password_hashed: str - Hashed password of the user. It is made of three mandatory fields, where the dollar sign is the field separator. The structure is: $id$salt$encrypted Only id 6 (SHA512) is supported. Salt minimum size is 2. reference: https://www.man7.org/linux/man-pages/man3/crypt.3.html
        :display_name: str - The display name for this user.
        :max_invalid_login: int - This attribute is the maximum number of consecutive and invalid login attempts before an account is suspended (lockedout). Zero disables escalation on login failure.
        :suspension_time: int - This attribute is the duration of UID suspension following consecutive invalid login attempts. Setting the value to 0 disables this behavior.
        :timeout: int - This attribute is the Session Time Out Interval. If there are no messages between the user and the NE over the Time Out interval, the session is logged off. Setting the value to 0 disables this attribute (meaning the session will not time out).
        :password_aging_interval: int - This attribute is the Password Aging Interval. Setting the value to 0 disables password aging.
        :enabled: bool - Enable switch for the user, allows admins to explicitly disable users.
        :force_password_change: bool - Allows administrator to force user to change password on next login.
        :max_sessions: int - This attribute specifies the maximum number of sessions allowed for this user.
        :user_group: unknown - Associated user groups for this user.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
    """

    password = kwargs.get('password', None)
    password_hashed = kwargs.get('password_hashed', None)
    display_name = kwargs.get('display_name', None)
    max_invalid_login = kwargs.get('max_invalid_login', None)
    suspension_time = kwargs.get('suspension_time', None)
    timeout = kwargs.get('timeout', None)
    password_aging_interval = kwargs.get('password_aging_interval', None)
    enabled = kwargs.get('enabled', None)
    force_password_change = kwargs.get('force_password_change', None)
    max_sessions = kwargs.get('max_sessions', None)
    user_group = kwargs.get('user_group', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user": [
                        {
                            "user-name": user_name,
                            "password": password,
                            "password-hashed": password_hashed,
                            "display-name": display_name,
                            "max-invalid-login": max_invalid_login,
                            "suspension-time": suspension_time,
                            "timeout": timeout,
                            "password-aging-interval": password_aging_interval,
                            "enabled": enabled,
                            "force-password-change": force_password_change,
                            "max-sessions": max_sessions,
                            "user-group": user_group,
                            "alarm-report-control": alarm_report_control,
                            "label": label
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_user(handle, user_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_name: The name of the user.
    :type user_name: str
    """

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user": [
                        {
                            "user-name": user_name
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_user(handle, user_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_name: The name of the user.
    :type user_name: str
    """

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user": [
                        {
                            "user-name": user_name,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def create_user_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Name of the group.
    :type name: str

    **Optional Parameters**:

        :description: str - Long description of the user group.
    """

    description = kwargs.get('description', None)

    object_name = 'User-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user-group": [
                        {
                            "name": name,
                            "description": description
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def update_user_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Name of the group.
    :type name: str

    **Optional Parameters**:

        :description: str - Long description of the user group.
    """

    description = kwargs.get('description', None)

    object_name = 'User-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user-group": [
                        {
                            "name": name,
                            "description": description
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_user_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Name of the group.
    :type name: str
    """

    object_name = 'User-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user-group": [
                        {
                            "name": name
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_user_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: Name of the group.
    :type name: str
    """

    object_name = 'User-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "user-group": [
                        {
                            "name": name,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'delete', request)
    return response


def update_security_policy(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :secure_mode: bool - If enabled, non-secure protocols are not supported. If disabled, non-secure protocols can be used, including: - HTTP protocol for file transfer, REST API, or any other HTTP based application - FTP protocol for file transfer - SNMPv2c or SNMPv3 without encryption  Enabling secure-mode will be rejected if any non-secure protocol is in use.
        :strict_password_check: bool - If enabled, ensures the strict password complexity rules. Including: - minimum length of 8 characters (by default, configurable via the minimum-password-length policy) - at least one lower case letter (a-z) - at least one upper case letter (A-Z) - at least one number (0-9) - at least one symbol () - user name cannot be part of the password If disabled, all these rules are not enforced, except: - minimum length is 1 character (by default, configurable via the minimum-password-length policy) Once enabled, this policy only has impact on newly defined passwords.
        :minimum_password_length: int - Configurable minimum length for user passwords. When a password is changed, the password length will be verified according with this policy. Note that changing this policy will not have impact on already set passwords, only on newly set passwords. The default value will depend on whether the policy strict-password-check is enabled or not (min length is 8 if enabled, 1 if disabled), but the user is able to override this value by editing this policy manually. Note: this policy can only be enforced when the password is provided in a non-hashed way.
        :ssh_authentication_method: str - The method used to authenticate user for SSH access. Note: For two-factor authentication, use public-key method and employ PIN/password-protected hardware device (e.g.: smart card or USB token.)
        :enforce_password_history_check: bool - If enabled, ensures that a new password being set cannot match any of the previous N passwords for the user. N is configurable through password-history-size. If disabled, password repetition is allowed. Once enabled, this policy only has impact on newly defined passwords.
        :password_history_size: int - The number of passwords to store for password reuse checking.
        :aaa_authentication_method: str - Specify authentication method for the user login to the NE.
        :aaa_authorization_method: str - Specify authorization policy for the logged user. If the user changes this parameter, it should logout and login again to apply the rules.
        :ssh_strict_host_key_checking: str - Specify the strictness of remote ssh/sftp/scp host identity checking.
        :ssh_key_aging_interval: int - This policy defines the ssh-authorized-keys aging interval. Setting the value to 0 disables ssh-authorized-keys aging. This affects the expiration date of all ssh-authorized-keys. Once aging is enabled, the expiration date is calculated from current time, for previously configured keys, and from configuration time, for newly configured keys.
        :root_password: str - The password of the root user.
        :console_user_password: str - The password of the console-user.
        :console_user_enabled: bool - A switch to enable/disable console-user. The console-user account is an emergency account that is only usable through the serial console. Disabling this account may put the device in a position where recovery is not possible, so it is recommended to keep this account enabled.
        :csp_symmetrical_key: str - Critical Security Parameters symmetrical key.
        :disable_user_lockout: bool - This policy allows to enable/disable user lockout when multiple invalid logins are detected. The number of invalid logins that trigger the lockout is configurable at the individual user level with the max-invalid-logins parameter. The time the user is locked-out is also configurable at user level with the suspension-time parameter.
        :supported_tls_version: str - Transport Layer Security (TLS) supported version(s). Changing this attribute will not affect existing connections.
        :crl_based_revocation: bool - This policy allows to enable/disable CRL-based certificate revocation.
        :crl_download_timeout: int - Specifies the maximum time to wait (in seconds) for automatic CRL downloads. Note: This timeout does not apply to manual CRL downloads.
        :ocsp_based_revocation: bool - This policy defines whether OCSP responders can be consulted for certificate revocation checking.
        :default_user_group: unknown - Default roles for users access.
        :ssh_ciphers: str - Allowed symmetric ciphers for SSH.
        :ssh_macs: str - Allowed message authentication code algorithms for SSH.
        :ssh_key_exchanges: str - Allowed key exchange algorithms for SSH.
        :ssh_host_key_algorithms: str - Allowed host key algorithms for SSH.
        :ssh_public_key_algorithms: str - Allowed public key algorithms for SSH.
        :tls_1_2_cipher_suites: str - Supported TLS 1.2 cipher suites. Changing this attribute will not affect existing connections.
        :tls_1_3_cipher_suites: str - Supported TLS 1.3 cipher suites. Changing this attribute will not affect existing connections. TLS_CHACHA20_POLY1305_SHA256 note: If present and requested by the client, it will be prioritized regardless of cipher-suite order.
        :tls_curves: str - Supported elliptic curve algorithms. The tls-curve algorithm affects both key-exchange and authentication stages of TLS handshake. Changing this attribute will not affect existing connections. Applies to both TLS 1.2 and 1.3. NOTE: Restricting curves can cause interoperability issues. TLS 1.2 remark: if the configured curve is not sent by the client, handshake may fail. TLS 1.3 remark: for the Authentication stage, it is possible that the server selects another curve different from the certificate signing algorithm.
        :db_passphrase: str - Passphrase used for encrypting and decrypting DB snapshots. For each command associated with DB snapshots (backup, restore, etc), this db-passphrase will be used, except when it is directly provided in each command. Automatic DB snapshots will not be enabled until this parameter is set.
    """

    secure_mode = kwargs.get('secure_mode', None)
    strict_password_check = kwargs.get('strict_password_check', None)
    minimum_password_length = kwargs.get('minimum_password_length', None)
    ssh_authentication_method = kwargs.get('ssh_authentication_method', None)
    enforce_password_history_check = kwargs.get('enforce_password_history_check', None)
    password_history_size = kwargs.get('password_history_size', None)
    aaa_authentication_method = kwargs.get('aaa_authentication_method', None)
    aaa_authorization_method = kwargs.get('aaa_authorization_method', None)
    ssh_strict_host_key_checking = kwargs.get('ssh_strict_host_key_checking', None)
    ssh_key_aging_interval = kwargs.get('ssh_key_aging_interval', None)
    root_password = kwargs.get('root_password', None)
    console_user_password = kwargs.get('console_user_password', None)
    console_user_enabled = kwargs.get('console_user_enabled', None)
    csp_symmetrical_key = kwargs.get('csp_symmetrical_key', None)
    disable_user_lockout = kwargs.get('disable_user_lockout', None)
    supported_tls_version = kwargs.get('supported_tls_version', None)
    crl_based_revocation = kwargs.get('crl_based_revocation', None)
    crl_download_timeout = kwargs.get('crl_download_timeout', None)
    ocsp_based_revocation = kwargs.get('ocsp_based_revocation', None)
    default_user_group = kwargs.get('default_user_group', None)
    ssh_ciphers = kwargs.get('ssh_ciphers', None)
    ssh_macs = kwargs.get('ssh_macs', None)
    ssh_key_exchanges = kwargs.get('ssh_key_exchanges', None)
    ssh_host_key_algorithms = kwargs.get('ssh_host_key_algorithms', None)
    ssh_public_key_algorithms = kwargs.get('ssh_public_key_algorithms', None)
    tls_1_2_cipher_suites = kwargs.get('tls_1_2_cipher_suites', None)
    tls_1_3_cipher_suites = kwargs.get('tls_1_3_cipher_suites', None)
    tls_curves = kwargs.get('tls_curves', None)
    db_passphrase = kwargs.get('db_passphrase', None)

    object_name = 'Security-Policy'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "security-policies": {
                        "secure-mode": secure_mode,
                        "strict-password-check": strict_password_check,
                        "minimum-password-length": minimum_password_length,
                        "ssh-authentication-method": ssh_authentication_method,
                        "enforce-password-history-check": enforce_password_history_check,
                        "password-history-size": password_history_size,
                        "aaa-authentication-method": aaa_authentication_method,
                        "aaa-authorization-method": aaa_authorization_method,
                        "ssh-strict-host-key-checking": ssh_strict_host_key_checking,
                        "ssh-key-aging-interval": ssh_key_aging_interval,
                        "root-password": root_password,
                        "console-user-password": console_user_password,
                        "console-user-enabled": console_user_enabled,
                        "csp-symmetrical-key": csp_symmetrical_key,
                        "disable-user-lockout": disable_user_lockout,
                        "supported-tls-version": supported_tls_version,
                        "crl-based-revocation": crl_based_revocation,
                        "crl-download-timeout": crl_download_timeout,
                        "ocsp-based-revocation": ocsp_based_revocation,
                        "default-user-group": default_user_group,
                        "ssh-ciphers": ssh_ciphers,
                        "ssh-macs": ssh_macs,
                        "ssh-key-exchanges": ssh_key_exchanges,
                        "ssh-host-key-algorithms": ssh_host_key_algorithms,
                        "ssh-public-key-algorithms": ssh_public_key_algorithms,
                        "tls-1.2-cipher-suites": tls_1_2_cipher_suites,
                        "tls-1.3-cipher-suites": tls_1_3_cipher_suites,
                        "tls-curves": tls_curves,
                        "db-passphrase": db_passphrase
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_security_policy(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'Security-Policy'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "system": {
                "security": {
                    "security-policies": {}
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_dsc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'DSC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "dsc": [
                    {
                        "name": name,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_dsc(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'DSC'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "dsc": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def update_dsc_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param carriers: The carrier associated to this facility. Possible values can be any card/resources/supported-carriers.
    :type carriers: str
    :param rate: Carried signal basic rate class
    :type rate: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :instance_id: int - For identifying the dsc-group logic number, is added to the dsc-group model for creation. The attribute is optional and will be automatically created if not specified. The maximum value of the instance-id will be calculated based on the capacity of the line mode and the dsc-group rate (ex: for creating an 100G dsc-group from 400G 16QAM line mode, instance can be between 1 and 4)
        :group_id: int - Optional parameter on dsc-group creation, specifies the dsc-group group number that the dsc is a member of for a given optical-carrier. If not provided, it is automatically assigned by system. (ex: for creating an 100G dsc-group from 400G 16QAM line mode, group-id can be 1/3/5/7)
        :pre_fec_q_sig_deg_threshold: str - The threshold based on which the PRE-FEC-Q-SIGNAL-DEGRADE alarm is raised. 0 implies threshold crossing alarming disabled. Specific sub-range is per carrier use-case.
        :pre_fec_q_sig_deg_hysteresis: str - Hysteresis to account for raising of the PRE-FEC-Q-SIGNAL-DEGRADE alarm.
        :post_fec_q_sig_deg_threshold: str - The threshold based on which the POST-FEC-Q-SIGNAL-DEGRADE alarm is raised.
        :post_fec_q_sig_deg_hysteresis: str - Hysteresis to account for raising of the POST-FEC-Q-SIGNAL-DEGRADE alarm.
        :dgd_high_threshold: int - The threshold to raise the DGD-OORH alarm.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    carriers = kwargs.get('carriers', None)
    rate = kwargs.get('rate', None)
    instance_id = kwargs.get('instance_id', None)
    group_id = kwargs.get('group_id', None)
    pre_fec_q_sig_deg_threshold = kwargs.get('pre_fec_q_sig_deg_threshold', None)
    pre_fec_q_sig_deg_hysteresis = kwargs.get('pre_fec_q_sig_deg_hysteresis', None)
    post_fec_q_sig_deg_threshold = kwargs.get('post_fec_q_sig_deg_threshold', None)
    post_fec_q_sig_deg_hysteresis = kwargs.get('post_fec_q_sig_deg_hysteresis', None)
    dgd_high_threshold = kwargs.get('dgd_high_threshold', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'DSC-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "dsc-group": [
                    {
                        "name": name,
                        "carriers": carriers,
                        "rate": rate,
                        "instance-id": instance_id,
                        "group-id": group_id,
                        "pre-fec-q-sig-deg-threshold": pre_fec_q_sig_deg_threshold,
                        "pre-fec-q-sig-deg-hysteresis": pre_fec_q_sig_deg_hysteresis,
                        "post-fec-q-sig-deg-threshold": post_fec_q_sig_deg_threshold,
                        "post-fec-q-sig-deg-hysteresis": post_fec_q_sig_deg_hysteresis,
                        "dgd-high-threshold": dgd_high_threshold,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_dsc_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'DSC-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "dsc-group": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


