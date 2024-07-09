import gxutils
#
# auto-generated pixi build code file
# Build: G40_R6_2_0 | Yang: infinera
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


def create_tom(handle, value, required_type, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param value: Value of the advanced parameter.
    :type value: str
    :param required_type: The type of the TOM.
    :type required_type: str

    **Optional Parameters**:

        :card_name: str - Card identifier.
        :port_name: str - Port name.
        :serdes_name: str - Name of the advanced parameter.
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


def create_super_channel(handle, , **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :contention_check_status: str - Contention Check state, set via DNA in openwave mode. Only applicable if openwave-contention-check is enabled at super-channel-group level.
        :carriers: str - A list of carriers that are bound to this superchannel. Possible values can be any card/resources/supported-carriers.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :carrier_mode: str - An acronymized code (handle) that is indicative of the optical carrier line mode (4-tuple) combination. The format is as follows:    <Capacity><ClientMode>.<Baud Rate><Application ID> Examples:    - 600E.84P    - 100X.73U    - 325M.66P
    """

    name = kwargs.get('name', None)
    contention_check_status = kwargs.get('contention_check_status', None)
    carriers = kwargs.get('carriers', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    carrier_mode = kwargs.get('carrier_mode', None)

    object_name = 'Super-Channel'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "super-channel": [
                    {
                        "name": name,
                        "contention-check-status": contention_check_status,
                        "carriers": carriers,
                        "label": label,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "carrier-mode": carrier_mode
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'create', request)
    return response


def get_super_channel(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Super-Channel'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "super-channel": [
                    {
                        "name": name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'get', request)
    return response


def delete_super_channel(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Super-Channel'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "super-channel": [
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


def update_super_channel_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :line_system_mode: str - Indicates the specific mode of power control configured on the L1 transponder, and specifically, on this particular SCG port within the L1 transponder. The attribute indicates the L1 <-> L0 local power controls to adjust the Tx power from the L1 transponder towards the L0 line-system card (such as a WSS or Mux or Amplifier).
        :openwave_contention_check: bool - Enables DNA assisted contention control mechanism in openwave mode.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :auto_in_service_enabled: bool - Auto-in-service switch for this facility.
        :valid_signal_time: int - Configurable time that represents a detection of a valid signal. Used for auto-in-service mechanism.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    line_system_mode = kwargs.get('line_system_mode', None)
    openwave_contention_check = kwargs.get('openwave_contention_check', None)
    label = kwargs.get('label', None)
    admin_state = kwargs.get('admin_state', None)
    auto_in_service_enabled = kwargs.get('auto_in_service_enabled', None)
    valid_signal_time = kwargs.get('valid_signal_time', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'Super-Channel-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "super-channel-group": [
                    {
                        "name": name,
                        "line-system-mode": line_system_mode,
                        "openwave-contention-check": openwave_contention_check,
                        "label": label,
                        "admin-state": admin_state,
                        "auto-in-service-enabled": auto_in_service_enabled,
                        "valid-signal-time": valid_signal_time,
                        "alarm-report-control": alarm_report_control
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'infinera', 'update', request)
    return response


def get_super_channel_group(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'Super-Channel-Group'
    manager = kwargs.get('manager')

    request = {
        "ne": {
            "facilities": {
                "super-channel-group": [
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
        :lldp_admin_status: str - LLDP operational mode for this port.
        :lldp_ingress_mode: str - If lldp enabled, define what is the LLDP behavior for this direction.
        :lldp_egress_mode: str - If lldp enabled, define what is the LLDP behavior for this direction.
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
    lldp_admin_status = kwargs.get('lldp_admin_status', None)
    lldp_ingress_mode = kwargs.get('lldp_ingress_mode', None)
    lldp_egress_mode = kwargs.get('lldp_egress_mode', None)

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
                        "test-signal-monitoring": test_signal_monitoring,
                        "lldp-admin-status": lldp_admin_status,
                        "lldp-ingress-mode": lldp_ingress_mode,
                        "lldp-egress-mode": lldp_egress_mode
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
        :sop_data_collection: str - Controls enabling/disabling sop data collection, providing the collection interval in ms.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :media_interface: str - Media interface type of ZR tom.
        :grid_spacing: str - Fixed Grid tunability for new 3rd party TOM.
        :loopback: str - Loopback mode.Useful to debug on the fiber connection.
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
    loopback = kwargs.get('loopback', None)
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
                        "loopback": loopback,
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
                        "propagate-shutdown-holdoff-timer": propagate_shutdown_holdoff_timer
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


def create_lo_odu(handle, odu_type, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param odu_type: The protocol type of the ODUk/ODUCn client.
    :type odu_type: str

    **Optional Parameters**:

        :name: str - A generic, configurable name for every facility.
        :direction: str - Diagnostics direction.Can be ingress or egress.
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
        :client_signal_type: str - Client signal type for ODUflex  CBR client. Applied to 200/400 GBE client on CHM1R. It is set automatically for the client side ODU, and need to be configured by the user at line side ODUj. Used for rate matching and bandwidth validation in the odu cross connection.
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

    object_name = 'LO-ODU'
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


def get_lo_odu(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'LO-ODU'
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


def delete_lo_odu(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param name: A generic, configurable name for every facility.
    :type name: str
    """

    object_name = 'LO-ODU'
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

    source = /ioa-ne:ne/ioa-ne:facilities/ioa-ne:odu[ioa-ne:name='{source}']
    destination = /ioa-ne:ne/ioa-ne:facilities/ioa-ne:odu[ioa-ne:name='{destination}']

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
        :osc_less: str - OSC-less mode is required to provide interworking with systems with no compatible OSC or spans with losses not compatible with the OSC budget.
        :fiber_type_rx: str - Fiber Type (OTS receiver) allows PCL to know the 'intercept' and 'slope'.
        :fiber_type_tx: str - Fiber Type (OTS transmitter) allows PCL to know the 'intercept' and 'slope'.
        :fiber_length_tx: str - Transmitting Fiber Length
        :fiber_length_rx: str - Receiving Fiber Length.
        :fiber_spectral_attenuation_tilt_tx: str - Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz.
        :fiber_spectral_attenuation_tilt_rx: str - Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz.
        :raman_coefficient_tx: str - Raman coefficient per Terahertz. Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz. Required for tilt control (if tilt-control-mode = auto). Configuration mode depends on tilt-control-mode.
        :raman_coefficient_rx: str - Raman coefficient per Terahertz. Since different transmission bands are supported, it is simpler to enter this parameter independent of the transmission bandwidth, hence per Terahertz. Required for tilt control (if tilt-control-mode = auto). Configuration mode depends on tilt-control-mode.
        :span_loss_receive: str - Fiber loss on the receiver side. (OTS-sk) This is only the loss of the fiber.
        :external_attenuation_tx: str - External padding attenuation at transmitting direction. Required for tilt control.
        :span_loss_aging_margin_rx: str - In native operating-mode: used by system for defining value of NMC input power range and span loss high alarm.
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
    osc_less = kwargs.get('osc_less', None)
    fiber_type_rx = kwargs.get('fiber_type_rx', None)
    fiber_type_tx = kwargs.get('fiber_type_tx', None)
    fiber_length_tx = kwargs.get('fiber_length_tx', None)
    fiber_length_rx = kwargs.get('fiber_length_rx', None)
    fiber_spectral_attenuation_tilt_tx = kwargs.get('fiber_spectral_attenuation_tilt_tx', None)
    fiber_spectral_attenuation_tilt_rx = kwargs.get('fiber_spectral_attenuation_tilt_rx', None)
    raman_coefficient_tx = kwargs.get('raman_coefficient_tx', None)
    raman_coefficient_rx = kwargs.get('raman_coefficient_rx', None)
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
                        "osc-less": osc_less,
                        "fiber-type-rx": fiber_type_rx,
                        "fiber-type-tx": fiber_type_tx,
                        "fiber-length-tx": fiber_length_tx,
                        "fiber-length-rx": fiber_length_rx,
                        "fiber-spectral-attenuation-tilt-tx": fiber_spectral_attenuation_tilt_tx,
                        "fiber-spectral-attenuation-tilt-rx": fiber_spectral_attenuation_tilt_rx,
                        "raman-coefficient-tx": raman_coefficient_tx,
                        "raman-coefficient-rx": raman_coefficient_rx,
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
        :pilot_tone_span_loss: str - The calculated span-loss based on Pilot Tone.
        :delta_pointloss: str - Delta Pointloss (Rx) Additional attenuation that can be determined after turning up pumps. This is the fiber contribution for the pointloss: to be fine tuned in the field. This additional optical attenuation may be due to e.g. bad splice at dwdm-line Rx, higher att. than 0.1 dB.
        :connected_reference: int - Indicates the degree the Raman is connected to. In ILA node-type(s), the direction the Raman is connected to (1 means direction 1-2, 2 means 2-1).
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :external_attenuation_rx: str - External Attenuation, configured by the user.
        :span_loss_transmit: str - Fiber loss on the transmitter side (OTS-so). This is only the loss of the fiber. Additional loss such as coming from patch panel is entered via the external-attenuation parameters.
    """

    required_fiber_type_rx = kwargs.get('required_fiber_type_rx', None)
    fiber_length_rx = kwargs.get('fiber_length_rx', None)
    span_loss_receive = kwargs.get('span_loss_receive', None)
    pilot_tone_span_loss = kwargs.get('pilot_tone_span_loss', None)
    delta_pointloss = kwargs.get('delta_pointloss', None)
    connected_reference = kwargs.get('connected_reference', None)
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
                        "pilot-tone-span-loss": pilot_tone_span_loss,
                        "delta-pointloss": delta_pointloss,
                        "connected-reference": connected_reference,
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
        :width: int - Network Media Channel frequency width; unit is MHz. User must configure the 3 dB signal bandwidth. Only set by creation.
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


def update_comm_channel(handle, name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: Indicates the type of control channel.
    :type type: str
    :param parent: Parent object of the comm-channel.
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
        :server_port: str - AAA server port number.
        :server_port_authentication: str - AAA server authentication port number.
        :server_port_accounting: str - AAA server accounting port number.
        :shared_secret: str - The shared secret of the aaa server. The shared secret will be displayed as *.
        :role_supported: str - The configured roles for the AAA server.
        :enabled: bool - Enable switch for this aaa-server.
        :timeout: int - Specifies the response timeout of Access-Request messages sent to a AAA server in seconds.
        :retry: int - Specifies the number of attempted Access-Request messages to a single AAA server before failing authentication.
        :source_ip: str - Source IP address used for RADIUS communications.
        :common_password: str - Password used for RADIUS authorization after SSH public key authentication. If blank, username is reused as password for RADIUS authorization.
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
                            "common-password": common_password
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
        :server_port: str - AAA server port number.
        :server_port_authentication: str - AAA server authentication port number.
        :server_port_accounting: str - AAA server accounting port number.
        :shared_secret: str - The shared secret of the aaa server. The shared secret will be displayed as *.
        :role_supported: str - The configured roles for the AAA server.
        :enabled: bool - Enable switch for this aaa-server.
        :timeout: int - Specifies the response timeout of Access-Request messages sent to a AAA server in seconds.
        :retry: int - Specifies the number of attempted Access-Request messages to a single AAA server before failing authentication.
        :source_ip: str - Source IP address used for RADIUS communications.
        :common_password: str - Password used for RADIUS authorization after SSH public key authentication. If blank, username is reused as password for RADIUS authorization.
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
                            "common-password": common_password
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


def create_ntp_server(handle, , **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :ip_address: str - NTP Server IP address. Ipv4/Ipv6/hostname supported.
        :origin: str - NTP address assignment method, user can convert DHCP configured NTP entry into a manual configured by changing this attribute.
        :auth_key_id: str - Key ID to be used for this server.
        :label: str - User label.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    ip_address = kwargs.get('ip_address', None)
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

    **Optional Parameters**:

        :ip_address: str - NTP Server IP address. Ipv4/Ipv6/hostname supported.
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
    """

    enabled = kwargs.get('enabled', None)
    port = kwargs.get('port', None)
    annotate_cli_name = kwargs.get('annotate_cli_name', None)
    hello_timeout = kwargs.get('hello_timeout', None)

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
                        "hello-timeout": hello_timeout
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
        :port: int - The port which listens for gNMI access via gRPC.
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


def create_user(handle, , **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :user_name: str - The name of the user.
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

    user_name = kwargs.get('user_name', None)
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

    **Optional Parameters**:

        :user_name: str - The name of the user.
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


def create_user_group(handle, , **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :name: str - Name of the group.
        :description: str - Long description of the user group.
    """

    name = kwargs.get('name', None)
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

    **Optional Parameters**:

        :name: str - Name of the group.
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

        :secure_mode: bool - If enabled, non-secure protocols are not supported. If disabled, non-secure protocols can be used, including: - HTTP protocol for file transfer, REST API, or any other HTTP based application - FTP protocol for file transfer - SNMPv2c or SNMPv3 without encryption  Enabling secure-mode will be rejected if any non-secure protocol is in use. Note: exception for SNMPv2c, which is allowed outside secure mode if system is in FIPS mode.
        :strict_password_check: bool - If enabled, ensures the strict password complexity rules. Including: - minimum length of 8 characters (by default, configurable via the minimum-password-length policy) - at least one lower case letter (a-z) - at least one upper case letter (A-Z) - at least one number (0-9) - at least one symbol () - user name cannot be part of the password If disabled, all these rules are not enforced, except: - minimum length is 1 character (by default, configurable via the minimum-password-length policy) Once enabled, this policy only has impact on newly defined passwords.
        :minimum_password_length: int - Configurable minimum length for user passwords. When a password is changed, the password length will be verified according with this policy. Note that changing this policy will not have impact on already set passwords, only on newly set passwords. The default value will depend on whether the policy strict-password-check is enabled or not (min length is 8 if enabled, 1 if disabled), but the user is able to override this value by editing this policy manually. Note: this policy can only be enforced when the password is provided in a non-hashed way.
        :ssh_authentication_method: str - The method used to authenticate user for SSH access. Note: For two-factor authentication, use public-key method and employ PIN/password-protected hardware device (e.g.: smart card or USB token.)
        :enforce_password_history_check: bool - If enabled, ensures that a new password being set cannot match any of the previous 5 password for the user. If disabled, password repetition is allowed. Once enabled, this policy only has impact on newly defined passwords.
        :aaa_authentication_method: str - Specify authentication method for the user login to the NE.
        :aaa_authorization_method: str - Specify authorization policy for the logged user. If the user changes this parameter, it should logout and login again to apply the rules.
        :ssh_strict_host_key_checking: str - Specify the strictness of remote ssh/sftp/scp host identity checking.
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
        :supported_signature_hash_algorithms: str - Supported hash algorithms for digital signatures for certificates. This applies to locally-managed certificates as well as certificates received from a remote peer. NOTE: If algorithms are removed from this list, any installed certificates using them will become unusable and transition to the 'unsupported' status, potentially disabling secure-applications and services. It also will prevent TLS connections to remote peers using unsupported signature hashes. Also, note that SHA-1 support is limited to root CA certificates.
        :db_passphrase: str - Passphrase used for encrypting and decrypting DB snapshots. For each command associated with DB snapshots (backup, restore, etc), this db-passphrase will be used, except when it is directly provided in each command. Automatic DB snapshots will not be enabled until this parameter is set.
    """

    secure_mode = kwargs.get('secure_mode', None)
    strict_password_check = kwargs.get('strict_password_check', None)
    minimum_password_length = kwargs.get('minimum_password_length', None)
    ssh_authentication_method = kwargs.get('ssh_authentication_method', None)
    enforce_password_history_check = kwargs.get('enforce_password_history_check', None)
    aaa_authentication_method = kwargs.get('aaa_authentication_method', None)
    aaa_authorization_method = kwargs.get('aaa_authorization_method', None)
    ssh_strict_host_key_checking = kwargs.get('ssh_strict_host_key_checking', None)
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
    supported_signature_hash_algorithms = kwargs.get('supported_signature_hash_algorithms', None)
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
                        "aaa-authentication-method": aaa_authentication_method,
                        "aaa-authorization-method": aaa_authorization_method,
                        "ssh-strict-host-key-checking": ssh_strict_host_key_checking,
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
                        "supported-signature-hash-algorithms": supported_signature_hash_algorithms,
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


