import gxutils
#
# auto-generated pixi build code file
# Build: G40_R6_1_20 | Yang: openconfig
#

def create_card(handle, component_name, chassis_name, slot_name, required_type, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param chassis_name: Chassis where this card is located.
    :type chassis_name: str
    :param slot_name: Slot where this card is located.
    :type slot_name: str
    :param required_type: Chassis/card type.
    :type required_type: str

    **Optional Parameters**:

        :required_subtype: str - The subtype of the Card/TOM
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :power_admin_state: str - Enable or disable power to the linecard
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param chassis_name: Chassis where this card is located.
    :type chassis_name: str
    :param slot_name: Slot where this card is located.
    :type slot_name: str
    :param required_type: Chassis/card type.
    :type required_type: str

    **Optional Parameters**:

        :required_subtype: str - The subtype of the Card/TOM
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :power_admin_state: str - Enable or disable power to the linecard

    **Example**
    ::
        gxctrl.create_card('g40', component_name='card-1-6', chassis_name='1', slot_name='6', required_type='CHM6', yang_type='openconfig')
    **Example**
    ::
        gxctrl.create_card('g40', component_name='card-1-6', chassis_name='1', slot_name='6', required_type='CHM6', yang_type='openconfig')
    """

    required_subtype = kwargs.get('required_subtype', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)
    alias_name = kwargs.get('alias_name', None)
    power_admin_state = kwargs.get('power_admin_state', None)

    object_name = 'Card'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "config": {
                        "name": component_name,
                        "chassis-name": chassis_name,
                        "slot-name": slot_name,
                        "required-type": required_type,
                        "required-subtype": required_subtype,
                        "alarm-report-control": alarm_report_control,
                        "label": label,
                        "alias-name": alias_name
                    },
                    "linecard": {
                        "config": {
                            "power-admin-state": power_admin_state
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_card(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str

    **Example**
    ::
        card_data = gxctrl.get_card('g40', 'card-1-6')
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str

    **Example**
    ::
        card_data = gxctrl.get_card('g40', 'card-1-6')
    """

    object_name = 'Card'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_card(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'Card'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "@operation": "delete"
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_tom(handle, component_name, phy_mode, required_subtype, form_factor_preconf, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param phy_mode: Configured Phy Mode.
    :type phy_mode: str
    :param required_subtype: The subtype of the Card/TOM
    :type required_subtype: str
    :param form_factor_preconf: Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not pluggable, then non-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system.
    :type form_factor_preconf: str

    **Optional Parameters**:

        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :serdes_name: str - Name of the advanced parameter.
        :value: str - Value of the advanced parameter.
        :enabled: bool - Turns power on / off to the transceiver -- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
        :fec_mode: str - The FEC mode indicates the mode of operation for the transceiver's FEC. This defines typical operational modes and does not aim to specify more granular FEC capabilities.
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param phy_mode: Configured Phy Mode.
    :type phy_mode: str
    :param required_subtype: The subtype of the Card/TOM
    :type required_subtype: str
    :param form_factor_preconf: Indicates the type of optical transceiver used on this port.  If the client port is built into the device and not pluggable, then non-pluggable is the corresponding state. If a device port supports multiple form factors (e.g. QSFP28 and QSFP+, then the value of the transceiver installed shall be reported. If no transceiver is present, then the value of the highest rate form factor shall be reported (QSFP28, for example).  The form factor is included in configuration data to allow pre-configuring a device with the expected type of transceiver ahead of deployment.  The corresponding state leaf should reflect the actual transceiver type plugged into the system.
    :type form_factor_preconf: str

    **Optional Parameters**:

        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :serdes_name: str - Name of the advanced parameter.
        :value: str - Value of the advanced parameter.
        :enabled: bool - Turns power on / off to the transceiver -- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
        :fec_mode: str - The FEC mode indicates the mode of operation for the transceiver's FEC. This defines typical operational modes and does not aim to specify more granular FEC capabilities.

    **Example**
    ::
        gxctrl.create_tom('g40', component_name='tom-1-6-T1', phy_mode='100G', required_subtype='TOM-100GMR-Q-LR4', form_factor_preconf='QSFP28', yang_type='openconfig')
    **Example**
    ::
        gxctrl.create_tom('g40', component_name='tom-1-6-T1', phy_mode='100G', required_subtype='TOM-100GMR-Q-LR4', form_factor_preconf='QSFP28', yang_type='openconfig')
    """

    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)
    alias_name = kwargs.get('alias_name', None)
    serdes_name = kwargs.get('serdes_name', None)
    value = kwargs.get('value', None)
    enabled = kwargs.get('enabled', None)
    fec_mode = kwargs.get('fec_mode', None)

    object_name = 'TOM'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "config": {
                        "name": component_name,
                        "phy-mode": phy_mode,
                        "required-subtype": required_subtype,
                        "alarm-report-control": alarm_report_control,
                        "label": label,
                        "alias-name": alias_name,
                        "serdes": [
                            {
                                "name": serdes_name,
                                "value": value
                            }
                        ]
                    },
                    "transceiver": {
                        "config": {
                            "enabled": enabled,
                            "form-factor-preconf": form_factor_preconf,
                            "fec-mode": fec_mode
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_tom(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'TOM'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_tom(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'TOM'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "@operation": "delete"
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_super_channel(handle, component_name, carriers, operational_mode, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param carriers: A list of carriers that are bound to this superchannel.    Possible values can be any card/resources/supported-carriers.
    :type carriers: str
    :param operational_mode: Vendor-specific mode identifier -- sets the operational mode for the channel.  The specified operational mode must exist in the list of supported operational modes supplied by the device
    :type operational_mode: int

    **Optional Parameters**:

        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param carriers: A list of carriers that are bound to this superchannel.    Possible values can be any card/resources/supported-carriers.
    :type carriers: str
    :param operational_mode: Vendor-specific mode identifier -- sets the operational mode for the channel.  The specified operational mode must exist in the list of supported operational modes supplied by the device
    :type operational_mode: int

    **Optional Parameters**:

        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.

    **Example**
    ::
        gxctrl.create_super_channel('g40', component_name='super-channel-SCH11', carriers='1-6-L1-1', operational_mode=488, yang_type='openconfig')
    **Example**
    ::
        gxctrl.create_super_channel('g40', component_name='super-channel-SCH11', carriers='1-6-L1-1', operational_mode=488, yang_type='openconfig')
    """

    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)

    object_name = 'Super-Channel'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "config": {
                        "name": component_name,
                        "carriers": carriers,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "label": label
                    },
                    "optical-channel": {
                        "config": {
                            "operational-mode": operational_mode
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_super_channel(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'Super-Channel'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_super_channel(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'Super-Channel'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "@operation": "delete"
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def update_super_channel_group(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :component_name: str - References the component name
        :auto_in_service_enabled: bool - Auto-in-service switch for this facility.
        :valid_signal_time: int - Configurable time that represents a detection of a valid signal. Used for auto-in-service mechanism.
        :line_system_mode: str - Indicates the specific mode of power control configured    on the L1 transponder, and specifically, on this particular SCG port within    the L1 transponder. The attribute indicates the L1 <-> L0 local power controls    to adjust the Tx power from the L1 transponder towards the L0 line-system    card (such as a WSS or Mux or Amplifier).
        :openwave_contention_check: bool - Enables DNA assisted contention control mechanism in openwave mode.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :enabled: bool - Turns power on / off to the transceiver -- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
    **Optional Parameters**:

        :component_name: str - References the component name
        :auto_in_service_enabled: bool - Auto-in-service switch for this facility.
        :valid_signal_time: int - Configurable time that represents a detection of a valid signal. Used for auto-in-service mechanism.
        :line_system_mode: str - Indicates the specific mode of power control configured    on the L1 transponder, and specifically, on this particular SCG port within    the L1 transponder. The attribute indicates the L1 <-> L0 local power controls    to adjust the Tx power from the L1 transponder towards the L0 line-system    card (such as a WSS or Mux or Amplifier).
        :openwave_contention_check: bool - Enables DNA assisted contention control mechanism in openwave mode.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :enabled: bool - Turns power on / off to the transceiver -- provides a means to power on/off the transceiver (in the case of SFP, SFP+, QSFP,...) or enable high-power mode (in the case of CFP, CFP2, CFP4) and is optionally supported (device can choose to always enable).  True = power on / high power, False = powered off
    """

    auto_in_service_enabled = kwargs.get('auto_in_service_enabled', None)
    valid_signal_time = kwargs.get('valid_signal_time', None)
    line_system_mode = kwargs.get('line_system_mode', None)
    openwave_contention_check = kwargs.get('openwave_contention_check', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)
    enabled = kwargs.get('enabled', None)

    object_name = 'Super-Channel-Group'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "config": {
                        "name": component_name,
                        "auto-in-service-enabled": auto_in_service_enabled,
                        "valid-signal-time": valid_signal_time,
                        "line-system-mode": line_system_mode,
                        "openwave-contention-check": openwave_contention_check,
                        "alarm-report-control": alarm_report_control,
                        "label": label
                    },
                    "transceiver": {
                        "config": {
                            "enabled": enabled
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_super_channel_group(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'Super-Channel-Group'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_optical_carrier_line(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str

    **Optional Parameters**:

        :frequency_offset: int - A super set range for line and client side carrier, specific sub-range is depend on application. Frequency-offset can be used for bright tuning    of the wavelengths.    Once set, the frequency will slowly change (over 1-10s) without affecting service.
        :pre_fec_q_sig_deg_threshold: decimal64 - The threshold based on which the PRE-FEC-Q-SIGNAL-DEGRADE alarm is raised.    0 implies threshold crossing alarming disabled.    Specific sub-range is per carrier use-case.
        :pre_fec_q_sig_deg_hysteresis: decimal64 - Hysteresis to account for raising of the PRE-FEC-Q-SIGNAL-DEGRADE alarm.
        :tx_cd: decimal64 - The configured transmit pre-compensation chromatic dispersion.
        :post_fec_q_sig_deg_threshold: decimal64 - The threshold based on which the POST-FEC-Q-SIGNAL-DEGRADE alarm is raised.
        :post_fec_q_sig_deg_hysteresis: decimal64 - Hysteresis to account for raising of the POST-FEC-Q-SIGNAL-DEGRADE alarm.
        :enable_advanced_parameters: bool - Controls enabling/disabling of configuring advanced parameters for this object.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :advanced_parameter_name: str - Name of the advanced parameter.
        :value: str - Value of the advanced parameter.
        :frequency: int - Frequency of the optical channel, expressed in MHz
        :target_output_power: str - Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel-milliwats)
        :state_of_polarization_sampling: union - Enables per-optical channel collection of SoP data. If SoP collection is enabled, this attribute indicates the sampling interval (i.e., sampling of the SoP data done by the DSP.)
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str

    **Optional Parameters**:

        :frequency_offset: int - A super set range for line and client side carrier, specific sub-range is depend on application. Frequency-offset can be used for bright tuning    of the wavelengths.    Once set, the frequency will slowly change (over 1-10s) without affecting service.
        :pre_fec_q_sig_deg_threshold: decimal64 - The threshold based on which the PRE-FEC-Q-SIGNAL-DEGRADE alarm is raised.    0 implies threshold crossing alarming disabled.    Specific sub-range is per carrier use-case.
        :pre_fec_q_sig_deg_hysteresis: decimal64 - Hysteresis to account for raising of the PRE-FEC-Q-SIGNAL-DEGRADE alarm.
        :tx_cd: decimal64 - The configured transmit pre-compensation chromatic dispersion.
        :post_fec_q_sig_deg_threshold: decimal64 - The threshold based on which the POST-FEC-Q-SIGNAL-DEGRADE alarm is raised.
        :post_fec_q_sig_deg_hysteresis: decimal64 - Hysteresis to account for raising of the POST-FEC-Q-SIGNAL-DEGRADE alarm.
        :enable_advanced_parameters: bool - Controls enabling/disabling of configuring advanced parameters for this object.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :advanced_parameter_name: str - Name of the advanced parameter.
        :value: str - Value of the advanced parameter.
        :frequency: int - Frequency of the optical channel, expressed in MHz
        :target_output_power: str - Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel-milliwats)
        :state_of_polarization_sampling: union - Enables per-optical channel collection of SoP data. If SoP collection is enabled, this attribute indicates the sampling interval (i.e., sampling of the SoP data done by the DSP.)
    """

    frequency_offset = kwargs.get('frequency_offset', None)
    pre_fec_q_sig_deg_threshold = kwargs.get('pre_fec_q_sig_deg_threshold', None)
    pre_fec_q_sig_deg_hysteresis = kwargs.get('pre_fec_q_sig_deg_hysteresis', None)
    tx_cd = kwargs.get('tx_cd', None)
    post_fec_q_sig_deg_threshold = kwargs.get('post_fec_q_sig_deg_threshold', None)
    post_fec_q_sig_deg_hysteresis = kwargs.get('post_fec_q_sig_deg_hysteresis', None)
    enable_advanced_parameters = kwargs.get('enable_advanced_parameters', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)
    advanced_parameter_name = kwargs.get('advanced_parameter_name', None)
    value = kwargs.get('value', None)
    frequency = kwargs.get('frequency', None)
    target_output_power = kwargs.get('target_output_power', None)
    state_of_polarization_sampling = kwargs.get('state_of_polarization_sampling', None)

    object_name = 'Optical-Carrier-Line'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "config": {
                        "name": component_name,
                        "frequency-offset": frequency_offset,
                        "pre-fec-q-sig-deg-threshold": pre_fec_q_sig_deg_threshold,
                        "pre-fec-q-sig-deg-hysteresis": pre_fec_q_sig_deg_hysteresis,
                        "tx-cd": tx_cd,
                        "post-fec-q-sig-deg-threshold": post_fec_q_sig_deg_threshold,
                        "post-fec-q-sig-deg-hysteresis": post_fec_q_sig_deg_hysteresis,
                        "enable-advanced-parameters": enable_advanced_parameters,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "label": label,
                        "advanced-parameter": [
                            {
                                "name": advanced_parameter_name,
                                "value": value
                            }
                        ]
                    },
                    "optical-channel": {
                        "config": {
                            "frequency": frequency,
                            "target-output-power": target_output_power,
                            "state-of-polarization-sampling": state_of_polarization_sampling
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_optical_carrier_line(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'Optical-Carrier-Line'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_optical_carrier_client(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str

    **Optional Parameters**:

        :frequency_offset: int - A super set range for line and client side carrier, specific sub-range is depend on application. Frequency-offset can be used for bright tuning    of the wavelengths.    Once set, the frequency will slowly change (over 1-10s) without affecting service.
        :pre_fec_q_sig_deg_threshold: decimal64 - The threshold based on which the PRE-FEC-Q-SIGNAL-DEGRADE alarm is raised.    0 implies threshold crossing alarming disabled.    Specific sub-range is per carrier use-case.
        :pre_fec_q_sig_deg_hysteresis: decimal64 - Hysteresis to account for raising of the PRE-FEC-Q-SIGNAL-DEGRADE alarm.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :frequency: int - Frequency of the optical channel, expressed in MHz
        :target_output_power: str - Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel-milliwats)
        :state_of_polarization_sampling: union - Enables per-optical channel collection of SoP data. If SoP collection is enabled, this attribute indicates the sampling interval (i.e., sampling of the SoP data done by the DSP.)
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str

    **Optional Parameters**:

        :frequency_offset: int - A super set range for line and client side carrier, specific sub-range is depend on application. Frequency-offset can be used for bright tuning    of the wavelengths.    Once set, the frequency will slowly change (over 1-10s) without affecting service.
        :pre_fec_q_sig_deg_threshold: decimal64 - The threshold based on which the PRE-FEC-Q-SIGNAL-DEGRADE alarm is raised.    0 implies threshold crossing alarming disabled.    Specific sub-range is per carrier use-case.
        :pre_fec_q_sig_deg_hysteresis: decimal64 - Hysteresis to account for raising of the PRE-FEC-Q-SIGNAL-DEGRADE alarm.
        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :frequency: int - Frequency of the optical channel, expressed in MHz
        :target_output_power: str - Target output optical power level of the optical channel, expressed in increments of 0.01 dBm (decibel-milliwats)
        :state_of_polarization_sampling: union - Enables per-optical channel collection of SoP data. If SoP collection is enabled, this attribute indicates the sampling interval (i.e., sampling of the SoP data done by the DSP.)
    """

    frequency_offset = kwargs.get('frequency_offset', None)
    pre_fec_q_sig_deg_threshold = kwargs.get('pre_fec_q_sig_deg_threshold', None)
    pre_fec_q_sig_deg_hysteresis = kwargs.get('pre_fec_q_sig_deg_hysteresis', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)
    frequency = kwargs.get('frequency', None)
    target_output_power = kwargs.get('target_output_power', None)
    state_of_polarization_sampling = kwargs.get('state_of_polarization_sampling', None)

    object_name = 'Optical-Carrier-Client'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "config": {
                        "name": component_name,
                        "frequency-offset": frequency_offset,
                        "pre-fec-q-sig-deg-threshold": pre_fec_q_sig_deg_threshold,
                        "pre-fec-q-sig-deg-hysteresis": pre_fec_q_sig_deg_hysteresis,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "label": label
                    },
                    "optical-channel": {
                        "config": {
                            "frequency": frequency,
                            "target-output-power": target_output_power,
                            "state-of-polarization-sampling": state_of_polarization_sampling
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_optical_carrier_client(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'Optical-Carrier-Client'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def create_lo_odu(handle, channel_index, trib_protocol, parent_odu, tributary_slot_index, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param channel_index: Reference to the index of the logical channel
    :type channel_index: int
    :param trib_protocol: Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client-Port or Optical-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib-rate-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are:  rate class: 1G protocols: 1GE  rate class: 2.5G protocols: OC48, STM16  rate class: 10G protocols:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class: 40G protocols:  40GE, OC768, STM256, OTU3, ODU3  rate class: 100G protocols:  100GE, 100G MLG, OTU4, OTUCn, ODU4
    :type trib_protocol: str
    :param parent_odu: For low order ODUs, points to the the parent HO-ODU name.
    :type parent_odu: unknown
    :param tributary_slot_index: Indicates the first tributary slot index allocated to the client signal or logical channel in the assignment. Valid only when the assignment is to an OTN logical channel.
    :type tributary_slot_index: int

    **Optional Parameters**:

        :channel_description: str - Description of the logical channel
        :admin_state: str - Sets the admin state of the logical channel
        :logical_channel_type: str - The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
        :allocation: str - Allocation of the logical client channel to the tributary or sub-channel, expressed in Gbps. Please note that if the assignment is to an OTN logical channel, the allocation must be an integer multiplication to tributary-slot-granularity of the OTN logical channel.
    :param handle: gxctrl connection handle
    :type handle: str
    :param channel_index: Reference to the index of the logical channel
    :type channel_index: int
    :param trib_protocol: Protocol framing of the tributary signal. If this LogicalChannel is directly connected to a Client-Port or Optical-Channel, this is the protocol of the associated port. If the LogicalChannel is connected to other LogicalChannels, the TributaryProtocol of the LogicalChannels will define a specific mapping/demapping or multiplexing/demultiplexing function.  Not all protocols are valid, depending on the value of trib-rate-class.  The expectation is that the NMS will validate that a correct combination of rate class and protocol are specfied.  Basic combinations are:  rate class: 1G protocols: 1GE  rate class: 2.5G protocols: OC48, STM16  rate class: 10G protocols:  10GE LAN, 10GE WAN, OC192, STM64, OTU2, OTU2e,            OTU1e, ODU2, ODU2e, ODU1e  rate class: 40G protocols:  40GE, OC768, STM256, OTU3, ODU3  rate class: 100G protocols:  100GE, 100G MLG, OTU4, OTUCn, ODU4
    :type trib_protocol: str
    :param parent_odu: For low order ODUs, points to the the parent HO-ODU name.
    :type parent_odu: unknown
    :param tributary_slot_index: Indicates the first tributary slot index allocated to the client signal or logical channel in the assignment. Valid only when the assignment is to an OTN logical channel.
    :type tributary_slot_index: int

    **Optional Parameters**:

        :channel_description: str - Description of the logical channel
        :admin_state: str - Sets the admin state of the logical channel
        :logical_channel_type: str - The type / stage of the logical element determines the configuration and operational state parameters (PMs) available for the logical element
        :allocation: str - Allocation of the logical client channel to the tributary or sub-channel, expressed in Gbps. Please note that if the assignment is to an OTN logical channel, the allocation must be an integer multiplication to tributary-slot-granularity of the OTN logical channel.

    **Example**
    ::
        gxctrl.create_lo_odu('g40', channel_index=42, trib_protocol='PROT_ODU4i', parent_odu='odu-1-6-L1-1', tributary_slot_index=81, yang_type='openconfig')
    **Example**
    ::
        gxctrl.create_lo_odu('g40', channel_index=42, trib_protocol='PROT_ODU4i', parent_odu='odu-1-6-L1-1', tributary_slot_index=81, yang_type='openconfig')
    """

    channel_description = kwargs.get('channel_description', None)
    admin_state = kwargs.get('admin_state', None)
    logical_channel_type = kwargs.get('logical_channel_type', None)
    allocation = kwargs.get('allocation', None)

    object_name = 'LO-ODU'
    manager = kwargs.get('manager')

    logical_channel = gxutils.get_logical_index_from_aid(parent_odu)

    request = {
        "terminal-device": {
            "logical-channels": {
                "channel": [
                    {
                        "index": channel_index,
                        "config": {
                            "index": channel_index,
                            "description": channel_description,
                            "admin-state": admin_state,
                            "trib-protocol": trib_protocol,
                            "logical-channel-type": logical_channel_type
                        },
                        "logical-channel-assignments": {
                            "assignment": [
                                {
                                    "index": 1,
                                    "config": {
                                        "index": 1,
                                        "description": "preset",
                                        "assignment-type": "LOGICAL_CHANNEL",
                                        "logical-channel": logical_channel,
                                        "allocation": allocation,
                                        "tributary-slot-index": tributary_slot_index
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_lo_odu(handle, channel_index, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param channel_index: Reference to the index of the logical channel
    :type channel_index: int
    :param handle: gxctrl connection handle
    :type handle: str
    :param channel_index: Reference to the index of the logical channel
    :type channel_index: int
    """

    object_name = 'LO-ODU'
    manager = kwargs.get('manager')


    request = {
        "terminal-device": {
            "logical-channels": {
                "channel": [
                    {
                        "index": channel_index
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_lo_odu(handle, channel_index, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param channel_index: Reference to the index of the logical channel
    :type channel_index: int
    :param handle: gxctrl connection handle
    :type handle: str
    :param channel_index: Reference to the index of the logical channel
    :type channel_index: int
    """

    object_name = 'LO-ODU'
    manager = kwargs.get('manager')


    request = {
        "terminal-device": {
            "logical-channels": {
                "channel": [
                    {
                        "index": channel_index,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_xcon(handle, source, destination_index, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point between which the XCON needs to be created.
    :type source: int
    :param destination_index: Index of the destination channel between which the XCON needs to be created.
    :type destination_index: unknown

    **Optional Parameters**:

        :allocation: str - Allocation of the logical client channel to the tributary or sub-channel, expressed in Gbps. Please note that if the assignment is to an OTN logical channel, the allocation must be an integer multiplication to tributary-slot-granularity of the OTN logical channel.
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point between which the XCON needs to be created.
    :type source: int
    :param destination_index: Index of the destination channel between which the XCON needs to be created.
    :type destination_index: unknown

    **Optional Parameters**:

        :allocation: str - Allocation of the logical client channel to the tributary or sub-channel, expressed in Gbps. Please note that if the assignment is to an OTN logical channel, the allocation must be an integer multiplication to tributary-slot-granularity of the OTN logical channel.

    **Example**
    ::
        gxctrl.create_xcon('g40', source='ethernet-1-6-T1', destination_index=42, yang_type='openconfig')
    **Example**
    ::
        gxctrl.create_xcon('g40', source='ethernet-1-6-T1', destination_index=42, yang_type='openconfig')
    """

    allocation = kwargs.get('allocation', None)

    object_name = 'XCON'
    manager = kwargs.get('manager')

    channel_index = gxutils.get_logical_index_from_aid(source)

    request = {
        "terminal-device": {
            "logical-channels": {
                "channel": [
                    {
                        "index": channel_index,
                        "logical-channel-assignments": {
                            "assignment": [
                                {
                                    "index": 1,
                                    "config": {
                                        "index": 1,
                                        "description": "flexible",
                                        "assignment-type": "LOGICAL_CHANNEL",
                                        "logical-channel": destination_index,
                                        "allocation": allocation
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_xcon(handle, source, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point between which the XCON needs to be created.
    :type source: int
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point between which the XCON needs to be created.
    :type source: int
    """

    object_name = 'XCON'
    manager = kwargs.get('manager')

    channel_index = gxutils.get_logical_index_from_aid(source)

    request = {
        "terminal-device": {
            "logical-channels": {
                "channel": [
                    {
                        "index": channel_index,
                        "logical-channel-assignments": {
                            "assignment": [
                                {
                                    "index": 1
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_xcon(handle, source, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point between which the XCON needs to be created.
    :type source: int
    :param handle: gxctrl connection handle
    :type handle: str
    :param source: The source end-point between which the XCON needs to be created.
    :type source: int
    """

    object_name = 'XCON'
    manager = kwargs.get('manager')

    channel_index = gxutils.get_logical_index_from_aid(source)

    request = {
        "terminal-device": {
            "logical-channels": {
                "channel": [
                    {
                        "index": channel_index,
                        "logical-channel-assignments": {
                            "assignment": [
                                {
                                    "index": 1,
                                    "@operation": "delete"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def update_chassis(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param required_type: Chassis/card type.
    :type required_type: str

    **Optional Parameters**:

        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :chassis_location: str - User defined location
        :rack_name: str - User defined rack name (withing the location)
        :position_in_rack: int - Position of the chassis within the rack.
        :expected_pem_type: str - Defines what is the expected type of PEMs that this chassis will have. It is not possible to configure each PEM slot individually, as all PEMs need to be of the same type.
        :expected_fan_type: str - Defines what is the expected type of FANs that this chassis will have. It is not possible to configure each FAN slot individually, this needs to be done at the chassis level.
        :pem_under_voltage_threshold: decimal64 - Under voltage threshold on PEM input feed.
        :pem_over_voltage_threshold: decimal64 - Over voltage threshold on PEM input feed.
        :configured_ambient_temperature: int - Configured ambient temperature for the chassis, used to compute the FRU's power consumption.
        :configured_max_power_draw: decimal64 - User configured limit of power usable by this chassis.    If current-estimated-power-draw used in this chassis goes above the configured-max-power-draw,    the alarm PWRDRAW is raised. 10000W represents a 'very high' power draw that is beyond any    chassis possibilities, so having this value means this feature is disabled, and the alarm is never raised.
        :no_switchover: str - If enabled, the standby controller will be locked out from taking over the active card. This means no manual or autonomous switchovers will happen.
        :power_redundancy: str - Configuration of the PEM redundancy mode.
        :expected_serial_number: str - Inform the NC the serial number of a sub-chassis. For the main-chassis, the value is auto-filled with its own serial number.
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param required_type: Chassis/card type.
    :type required_type: str

    **Optional Parameters**:

        :admin_state: str - The administrative state of the managed object.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
        :label: str - User label.
        :alias_name: str - User defined alias for this entity. Must be an alphanumeric string with dash or underscore.
        :chassis_location: str - User defined location
        :rack_name: str - User defined rack name (withing the location)
        :position_in_rack: int - Position of the chassis within the rack.
        :expected_pem_type: str - Defines what is the expected type of PEMs that this chassis will have. It is not possible to configure each PEM slot individually, as all PEMs need to be of the same type.
        :expected_fan_type: str - Defines what is the expected type of FANs that this chassis will have. It is not possible to configure each FAN slot individually, this needs to be done at the chassis level.
        :pem_under_voltage_threshold: decimal64 - Under voltage threshold on PEM input feed.
        :pem_over_voltage_threshold: decimal64 - Over voltage threshold on PEM input feed.
        :configured_ambient_temperature: int - Configured ambient temperature for the chassis, used to compute the FRU's power consumption.
        :configured_max_power_draw: decimal64 - User configured limit of power usable by this chassis.    If current-estimated-power-draw used in this chassis goes above the configured-max-power-draw,    the alarm PWRDRAW is raised. 10000W represents a 'very high' power draw that is beyond any    chassis possibilities, so having this value means this feature is disabled, and the alarm is never raised.
        :no_switchover: str - If enabled, the standby controller will be locked out from taking over the active card. This means no manual or autonomous switchovers will happen.
        :power_redundancy: str - Configuration of the PEM redundancy mode.
        :expected_serial_number: str - Inform the NC the serial number of a sub-chassis. For the main-chassis, the value is auto-filled with its own serial number.
    """

    required_type = kwargs.get('required_type', None)
    admin_state = kwargs.get('admin_state', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)
    label = kwargs.get('label', None)
    alias_name = kwargs.get('alias_name', None)
    chassis_location = kwargs.get('chassis_location', None)
    rack_name = kwargs.get('rack_name', None)
    position_in_rack = kwargs.get('position_in_rack', None)
    expected_pem_type = kwargs.get('expected_pem_type', None)
    expected_fan_type = kwargs.get('expected_fan_type', None)
    pem_under_voltage_threshold = kwargs.get('pem_under_voltage_threshold', None)
    pem_over_voltage_threshold = kwargs.get('pem_over_voltage_threshold', None)
    configured_ambient_temperature = kwargs.get('configured_ambient_temperature', None)
    configured_max_power_draw = kwargs.get('configured_max_power_draw', None)
    no_switchover = kwargs.get('no_switchover', None)
    power_redundancy = kwargs.get('power_redundancy', None)
    expected_serial_number = kwargs.get('expected_serial_number', None)

    object_name = 'Chassis'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name,
                    "config": {
                        "name": component_name,
                        "required-type": required_type,
                        "admin-state": admin_state,
                        "alarm-report-control": alarm_report_control,
                        "label": label,
                        "alias-name": alias_name,
                        "chassis-location": chassis_location,
                        "rack-name": rack_name,
                        "position-in-rack": position_in_rack,
                        "expected-pem-type": expected_pem_type,
                        "expected-fan-type": expected_fan_type,
                        "pem-under-voltage-threshold": pem_under_voltage_threshold,
                        "pem-over-voltage-threshold": pem_over_voltage_threshold,
                        "configured-ambient-temperature": configured_ambient_temperature,
                        "configured-max-power-draw": configured_max_power_draw,
                        "no-switchover": no_switchover,
                        "power-redundancy": power_redundancy
                    },
                    "chassis": {
                        "config": {
                            "expected-serial-number": expected_serial_number
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_chassis(handle, component_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param component_name: References the component name
    :type component_name: str
    """

    object_name = 'Chassis'
    manager = kwargs.get('manager')

    request = {
        "components": {
            "component": [
                {
                    "name": component_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_system(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :motd_banner: str - The console message displayed after a user logs into the system.  They system may append additional standard information such as the current system date and time, uptime, last login timestamp, etc.
        :hostname: str - The hostname of the device -- should be a single domain label, without the domain.
        :login_banner: str - The console login message displayed before the login prompt, i.e., before a user logs into the system.
    **Optional Parameters**:

        :motd_banner: str - The console message displayed after a user logs into the system.  They system may append additional standard information such as the current system date and time, uptime, last login timestamp, etc.
        :hostname: str - The hostname of the device -- should be a single domain label, without the domain.
        :login_banner: str - The console login message displayed before the login prompt, i.e., before a user logs into the system.
    """

    motd_banner = kwargs.get('motd_banner', None)
    hostname = kwargs.get('hostname', None)
    login_banner = kwargs.get('login_banner', None)

    object_name = 'System'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "config": {
                "motd-banner": motd_banner,
                "hostname": hostname,
                "login-banner": login_banner
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_system(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'System'
    manager = kwargs.get('manager')

    request = {
        "system": {}
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_clock(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :timezone_name: str - The TZ database name to use for the system, such as 'Europe/Stockholm'.
    **Optional Parameters**:

        :timezone_name: str - The TZ database name to use for the system, such as 'Europe/Stockholm'.
    """

    timezone_name = kwargs.get('timezone_name', None)

    object_name = 'Clock'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "clock": {
                "config": {
                    "timezone-name": timezone_name
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_clock(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'Clock'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "clock": {}
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def create_aaa_radius(handle, server_address, server_priority, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: Reference to the configured address of the AAA server
    :type server_address: str
    :param server_priority: Reference to the configured address of the AAA server
    :type server_priority: uint32

    **Optional Parameters**:

        :timeout: int - Reference to the configured address of the AAA server
        :auth_port: int - Port number for authentication requests
        :acct_port: int - Port number for accounting requests
        :secret_key: str - The unencrypted shared key used between the authentication server and the device.
        :source_address: str - Source IP address to use in messages to the RADIUS server
        :retransmit_attempts: int - Number of times the system may resend a request to the RADIUS server when it is unresponsive
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: Reference to the configured address of the AAA server
    :type server_address: str
    :param server_priority: Reference to the configured address of the AAA server
    :type server_priority: uint32

    **Optional Parameters**:

        :timeout: int - Reference to the configured address of the AAA server
        :auth_port: int - Port number for authentication requests
        :acct_port: int - Port number for accounting requests
        :secret_key: str - The unencrypted shared key used between the authentication server and the device.
        :source_address: str - Source IP address to use in messages to the RADIUS server
        :retransmit_attempts: int - Number of times the system may resend a request to the RADIUS server when it is unresponsive

    **Example**
    ::
        gxctrl.create_aaa_radius('g40', '1.1.1.1', 2, timeout=5, auth_port=1812, acct_port=1813, source_address='auto')
    **Example**
    ::
        gxctrl.create_aaa_radius('g40', '1.1.1.1', 2, timeout=5, auth_port=1812, acct_port=1813, source_address='auto')
    """

    timeout = kwargs.get('timeout', None)
    auth_port = kwargs.get('auth_port', None)
    acct_port = kwargs.get('acct_port', None)
    secret_key = kwargs.get('secret_key', None)
    source_address = kwargs.get('source_address', None)
    retransmit_attempts = kwargs.get('retransmit_attempts', None)

    object_name = 'AAA-RADIUS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "server-groups": {
                    "server-group": [
                        {
                            "name": "RADIUS",
                            "config": {
                                "name": "RADIUS",
                                "type": "RADIUS"
                            },
                            "servers": {
                                "server": [
                                    {
                                        "address": server_address,
                                        "config": {
                                            "address": server_address,
                                            "timeout": timeout,
                                            "server-priority": server_priority
                                        },
                                        "radius": {
                                            "config": {
                                                "auth-port": auth_port,
                                                "acct-port": acct_port,
                                                "secret-key": secret_key,
                                                "source-address": source_address,
                                                "retransmit-attempts": retransmit_attempts
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_aaa_radius(handle, server_group_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    """

    object_name = 'AAA-RADIUS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "server-groups": {
                    "server-group": [
                        {
                            "name": server_group_name
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_aaa_radius(handle, server_group_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    """

    object_name = 'AAA-RADIUS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "server-groups": {
                    "server-group": [
                        {
                            "name": server_group_name,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_aaa_tacacs(handle, server_address, server_priority, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: Reference to the configured address of the AAA server
    :type server_address: str
    :param server_priority: This is used to sort the servers in the order of precedence
    :type server_priority: uint32

    **Optional Parameters**:

        :timeout: int - Reference to the configured address of the AAA server
        :port: int - Port number for authentication requests
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: Reference to the configured address of the AAA server
    :type server_address: str
    :param server_priority: This is used to sort the servers in the order of precedence
    :type server_priority: uint32

    **Optional Parameters**:

        :timeout: int - Reference to the configured address of the AAA server
        :port: int - Port number for authentication requests

    **Example**
    ::
        gxctrl.create_aaa_tacacs('g40', '2.2.2.2', 3, timeout=5, port=1815)
    **Example**
    ::
        gxctrl.create_aaa_tacacs('g40', '2.2.2.2', 3, timeout=5, port=1815)
    """

    timeout = kwargs.get('timeout', None)
    port = kwargs.get('port', None)

    object_name = 'AAA-TACACS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "server-groups": {
                    "server-group": [
                        {
                            "name": "TACACSPLUS",
                            "config": {
                                "name": "TACACSPLUS",
                                "type": "TACACS"
                            },
                            "servers": {
                                "server": [
                                    {
                                        "address": server_address,
                                        "config": {
                                            "address": server_address,
                                            "timeout": timeout,
                                            "server-priority": server_priority
                                        },
                                        "tacacs": {
                                            "config": {
                                                "port": port
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_aaa_tacacs(handle, server_group_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    """

    object_name = 'AAA-TACACS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "server-groups": {
                    "server-group": [
                        {
                            "name": server_group_name
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_aaa_tacacs(handle, server_group_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_group_name: Reference to configured name of the server group
    :type server_group_name: str
    """

    object_name = 'AAA-TACACS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "server-groups": {
                    "server-group": [
                        {
                            "name": server_group_name,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def update_ntp(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :enabled: bool - Enables the NTP protocol and indicates that the system should attempt to synchronize the system clock with an NTP server from the servers defined in the 'ntp/server' list.
        :enable_ntp_auth: bool - Enable or disable NTP authentication -- when enabled, the system will only use packets containing a trusted authentication key to synchronize the time.
    **Optional Parameters**:

        :enabled: bool - Enables the NTP protocol and indicates that the system should attempt to synchronize the system clock with an NTP server from the servers defined in the 'ntp/server' list.
        :enable_ntp_auth: bool - Enable or disable NTP authentication -- when enabled, the system will only use packets containing a trusted authentication key to synchronize the time.
    """

    enabled = kwargs.get('enabled', None)
    enable_ntp_auth = kwargs.get('enable_ntp_auth', None)

    object_name = 'NTP'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {
                "config": {
                    "enabled": enabled,
                    "enable-ntp-auth": enable_ntp_auth
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_ntp(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'NTP'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {}
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def create_ntp_key(handle, ntp_key_key_id, key_type, key_value, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param ntp_key_key_id: Reference to auth key-id list key
    :type ntp_key_key_id: int
    :param key_type: Encryption type used for the NTP authentication key
    :type key_type: str
    :param key_value: NTP authentication key value
    :type key_value: str

    **Optional Parameters**:
    :param handle: gxctrl connection handle
    :type handle: str
    :param ntp_key_key_id: Reference to auth key-id list key
    :type ntp_key_key_id: int
    :param key_type: Encryption type used for the NTP authentication key
    :type key_type: str
    :param key_value: NTP authentication key value
    :type key_value: str

    **Optional Parameters**:


    **Example**
    ::
        gxctrl.create_ntp_key('g40', 123, 'NTP_AUTH_MD5', 'myntpkeyval')

    **Example**
    ::
        gxctrl.create_ntp_key('g40', 123, 'NTP_AUTH_MD5', 'myntpkeyval')
    """


    object_name = 'NTP-Key'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {
                "ntp-keys": {
                    "ntp-key": [
                        {
                            "key-id": ntp_key_key_id,
                            "config": {
                                "key-id": ntp_key_key_id,
                                "key-type": key_type,
                                "key-value": key_value
                            }
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_ntp_key(handle, ntp_key_key_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param ntp_key_key_id: Reference to auth key-id list key
    :type ntp_key_key_id: int
    :param handle: gxctrl connection handle
    :type handle: str
    :param ntp_key_key_id: Reference to auth key-id list key
    :type ntp_key_key_id: int
    """

    object_name = 'NTP-Key'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {
                "ntp-keys": {
                    "ntp-key": [
                        {
                            "key-id": ntp_key_key_id
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_ntp_key(handle, ntp_key_key_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param ntp_key_key_id: Reference to auth key-id list key
    :type ntp_key_key_id: int
    :param handle: gxctrl connection handle
    :type handle: str
    :param ntp_key_key_id: Reference to auth key-id list key
    :type ntp_key_key_id: int
    """

    object_name = 'NTP-Key'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {
                "ntp-keys": {
                    "ntp-key": [
                        {
                            "key-id": ntp_key_key_id,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_ntp_server(handle, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address or hostname of the NTP server.
    :type server_address: str

    **Optional Parameters**:
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address or hostname of the NTP server.
    :type server_address: str

    **Optional Parameters**:


    **Example**
    ::
        gxctrl.create_ntp_server('g40', '4.4.4.4')

    **Example**
    ::
        gxctrl.create_ntp_server('g40', '4.4.4.4')
    """


    object_name = 'NTP-Server'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {
                "servers": {
                    "server": [
                        {
                            "address": server_address,
                            "config": {
                                "address": server_address
                            }
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_ntp_server(handle, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address or hostname of the NTP server.
    :type server_address: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address or hostname of the NTP server.
    :type server_address: str
    """

    object_name = 'NTP-Server'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {
                "servers": {
                    "server": [
                        {
                            "address": server_address
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_ntp_server(handle, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address or hostname of the NTP server.
    :type server_address: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address or hostname of the NTP server.
    :type server_address: str
    """

    object_name = 'NTP-Server'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "ntp": {
                "servers": {
                    "server": [
                        {
                            "address": server_address,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def update_grpc_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :enable: bool - Enables the gRPC server. The gRPC server is enabled by default
        :port: int - TCP port on which the gRPC server should listen
        :certificate_id: str - The certificate ID to be used for authentication
    **Optional Parameters**:

        :enable: bool - Enables the gRPC server. The gRPC server is enabled by default
        :port: int - TCP port on which the gRPC server should listen
        :certificate_id: str - The certificate ID to be used for authentication

    **Example**
    ::
        gxctrl.update_grpc_server('g40', enable=True, port=1014)
    **Example**
    ::
        gxctrl.update_grpc_server('g40', enable=True, port=1014)
    """

    enable = kwargs.get('enable', None)
    port = kwargs.get('port', None)
    certificate_id = kwargs.get('certificate_id', None)

    object_name = 'GRPC-Server'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "grpc-server": {
                "config": {
                    "enable": enable,
                    "port": port,
                    "certificate-id": certificate_id
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_grpc_server(handle, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str
    """

    object_name = 'GRPC-Server'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "grpc-server": {}
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def create_dns(handle, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str

    **Optional Parameters**:

    **Optional Parameters**:

    """


    object_name = 'DNS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "dns": {
                "config": {},
                "servers": {
                    "server": [
                        {
                            "address": server_address,
                            "config": {
                                "address": server_address
                            }
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def update_dns(handle, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str

    **Optional Parameters**:

    **Optional Parameters**:

    """


    object_name = 'DNS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "dns": {
                "config": {},
                "servers": {
                    "server": [
                        {
                            "address": server_address,
                            "config": {
                                "address": server_address
                            }
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_dns(handle, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str
    """

    object_name = 'DNS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "dns": {
                "servers": {
                    "server": [
                        {
                            "address": server_address
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_dns(handle, server_address, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param server_address: References the configured address of the DNS server
    :type server_address: str
    """

    object_name = 'DNS'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "dns": {
                "servers": {
                    "server": [
                        {
                            "address": server_address,
                            "@operation": "delete"
                        }
                    ]
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def update_lldp(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param handle: gxctrl connection handle
    :type handle: str

    **Optional Parameters**:

        :lldp_enabled: bool - System level state of the LLDP protocol.
        :hello_timer: int - 
        :suppress_tlv_advertisement: str - 
        :system_name: str - 
        :system_description: str - 
        :chassis_id: int - 
        :chassis_id_type: int - 
        :interface_name: str - 
        :interface_enabled: bool - 
    """

    lldp_enabled = kwargs.get('lldp_enabled', None)
    hello_timer = kwargs.get('hello_timer', None)
    suppress_tlv_advertisement = kwargs.get('suppress_tlv_advertisement', None)
    system_name = kwargs.get('system_name', None)
    system_description = kwargs.get('system_description', None)
    chassis_id = kwargs.get('chassis_id', None)
    chassis_id_type = kwargs.get('chassis_id_type', None)
    interface_enabled = kwargs.get('interface_enabled', None)

    object_name = 'LLDP'
    manager = kwargs.get('manager')

    request = {
        "lldp": {
            "config": {
                "enabled": lldp_enabled,
                "hello-timer": hello_timer,
                "suppress-tlv-advertisement": suppress_tlv_advertisement,
                "system-name": system_name,
                "system-description": system_description,
                "chassis-id": chassis_id,
                "chassis-id-type": chassis_id_type
            },
            "interfaces": {
                "interface": [
                    {
                        "name": interface_name,
                        "config": {
                            "name": interface_name,
                            "enabled": interface_enabled
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_lldp(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: 
    :type interface_name: str
    """

    object_name = 'LLDP'
    manager = kwargs.get('manager')

    request = {
        "lldp": {
            "interfaces": {
                "interface": [
                    {
                        "name": interface_name
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def create_static_route(handle, static_prefix, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str

    **Optional Parameters**:

        :vrf: str - VRF associated with this static route.
        :advertised: bool - When set to YES, the static route is advertised in the routing protocol. For OSPF, the static route will be advertised as an AS external route, if OSPF is configured as an ASBR.
        :label: str - User label.
        :next_hop_index: str - 
        :next_hop: str - 
        :metric: str - 
        :recurse: bool - 
    """

    vrf = kwargs.get('vrf', None)
    advertised = kwargs.get('advertised', None)
    label = kwargs.get('label', None)
    next_hop_index = kwargs.get('next_hop_index', None)
    next_hop = kwargs.get('next_hop', None)
    metric = kwargs.get('metric', None)
    recurse = kwargs.get('recurse', None)

    object_name = 'Static-Route'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix,
                        "config": {
                            "prefix": static_prefix,
                            "vrf": vrf,
                            "advertised": advertised,
                            "label": label
                        },
                        "next-hops": {
                            "next-hop": [
                                {
                                    "index": next_hop_index,
                                    "config": {
                                        "index": next_hop_index,
                                        "next-hop": next_hop,
                                        "metric": metric,
                                        "recurse": recurse
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def update_static_route(handle, static_prefix, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str

    **Optional Parameters**:

        :vrf: str - VRF associated with this static route.
        :advertised: bool - When set to YES, the static route is advertised in the routing protocol. For OSPF, the static route will be advertised as an AS external route, if OSPF is configured as an ASBR.
        :label: str - User label.
        :next_hop_index: str - 
        :next_hop: str - 
        :metric: str - 
        :recurse: bool - 
    """

    vrf = kwargs.get('vrf', None)
    advertised = kwargs.get('advertised', None)
    label = kwargs.get('label', None)
    next_hop = kwargs.get('next_hop', None)
    metric = kwargs.get('metric', None)
    recurse = kwargs.get('recurse', None)

    object_name = 'Static-Route'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix,
                        "config": {
                            "prefix": static_prefix,
                            "vrf": vrf,
                            "advertised": advertised,
                            "label": label
                        },
                        "next-hops": {
                            "next-hop": [
                                {
                                    "index": next_hop_index,
                                    "config": {
                                        "index": next_hop_index,
                                        "next-hop": next_hop,
                                        "metric": metric,
                                        "recurse": recurse
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_static_route(handle, static_prefix, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    """

    object_name = 'Static-Route'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_static_route(handle, static_prefix, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    """

    object_name = 'Static-Route'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_static_route_dcn(handle, static_prefix, interface, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param interface: 
    :type interface: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param interface: 
    :type interface: str

    **Optional Parameters**:

        :vrf: str - VRF associated with this static route.
        :advertised: bool - When set to YES, the static route is advertised in the routing protocol. For OSPF, the static route will be advertised as an AS external route, if OSPF is configured as an ASBR.
        :label: str - User label.
        :next_hop_index: str - 
        :next_hop: str - 
        :metric: str - 
        :recurse: bool - 
    """

    vrf = kwargs.get('vrf', None)
    advertised = kwargs.get('advertised', None)
    label = kwargs.get('label', None)
    next_hop_index = kwargs.get('next_hop_index', None)
    next_hop = kwargs.get('next_hop', None)
    metric = kwargs.get('metric', None)
    recurse = kwargs.get('recurse', None)

    object_name = 'Static-Route-DCN'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix,
                        "config": {
                            "prefix": static_prefix,
                            "vrf": vrf,
                            "advertised": advertised,
                            "label": label
                        },
                        "next-hops": {
                            "next-hop": [
                                {
                                    "index": next_hop_index,
                                    "config": {
                                        "index": next_hop_index,
                                        "next-hop": next_hop,
                                        "metric": metric,
                                        "recurse": recurse
                                    },
                                    "interface-ref": {
                                        "config": {
                                            "interface": interface
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def update_static_route_dcn(handle, static_prefix, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param interface: 
    :type interface: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param interface: 
    :type interface: str

    **Optional Parameters**:

        :vrf: str - VRF associated with this static route.
        :advertised: bool - When set to YES, the static route is advertised in the routing protocol. For OSPF, the static route will be advertised as an AS external route, if OSPF is configured as an ASBR.
        :label: str - User label.
        :next_hop_index: str - 
        :next_hop: str - 
        :metric: str - 
        :recurse: bool - 
    """

    vrf = kwargs.get('vrf', None)
    advertised = kwargs.get('advertised', None)
    label = kwargs.get('label', None)
    next_hop = kwargs.get('next_hop', None)
    metric = kwargs.get('metric', None)
    recurse = kwargs.get('recurse', None)
    interface = kwargs.get('interface', None)

    object_name = 'Static-Route-DCN'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix,
                        "config": {
                            "prefix": static_prefix,
                            "vrf": vrf,
                            "advertised": advertised,
                            "label": label
                        },
                        "next-hops": {
                            "next-hop": [
                                {
                                    "index": next_hop_index,
                                    "config": {
                                        "index": next_hop_index,
                                        "next-hop": next_hop,
                                        "metric": metric,
                                        "recurse": recurse
                                    },
                                    "interface-ref": {
                                        "config": {
                                            "interface": interface
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_static_route_dcn(handle, static_prefix, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    """

    object_name = 'Static-Route-DCN'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_static_route_dcn(handle, static_prefix, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param static_prefix: 
    :type static_prefix: str
    """

    object_name = 'Static-Route-DCN'
    manager = kwargs.get('manager')

    request = {
        "local-routes": {
            "static-routes": {
                "static": [
                    {
                        "prefix": static_prefix,
                        "@operation": "delete"
                    }
                ]
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_lo_mgmt(handle, type, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.
    :type type: str

    **Optional Parameters**:

        :subinterface_index: int - The index number of the subinterface -- used to address the logical interface
        :description: str - A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.
        :subinterface_enabled: bool - This leaf contains the configured, desired state of the interface.  Systems that implement the IF-MIB use the value of this leaf in the 'running' datastore to set IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected.
        :address_ip: str - 
        :address_prefix_length: int - 
        :ipv4_enabled: bool - 
        :ipv4_dhcp_client: bool - 
        :ipv6_enabled: bool - 
        :ipv6_dhcp_client: bool - 
    """

    subinterface_index = kwargs.get('subinterface_index', None)
    description = kwargs.get('description', None)
    subinterface_enabled = kwargs.get('subinterface_enabled', None)
    address_ip = kwargs.get('address_ip', None)
    address_prefix_length = kwargs.get('address_prefix_length', None)
    ipv4_enabled = kwargs.get('ipv4_enabled', None)
    ipv4_dhcp_client = kwargs.get('ipv4_dhcp_client', None)
    ipv6_enabled = kwargs.get('ipv6_enabled', None)
    ipv6_dhcp_client = kwargs.get('ipv6_dhcp_client', None)

    object_name = 'LO-MGMT'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": "LO-MGMT",
                    "config": {
                        "name": "LO-MGMT",
                        "type": type
                    },
                    "subinterfaces": {
                        "subinterface": [
                            {
                                "index": subinterface_index,
                                "config": {
                                    "index": subinterface_index,
                                    "description": description,
                                    "enabled": subinterface_enabled
                                },
                                "ipv4": {
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    },
                                    "config": {
                                        "enabled": ipv4_enabled,
                                        "dhcp-client": ipv4_dhcp_client
                                    }
                                },
                                "ipv6": {
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    },
                                    "config": {
                                        "enabled": ipv6_enabled,
                                        "dhcp-client": ipv6_dhcp_client
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def update_lo_mgmt(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.
    :type type: str

    **Optional Parameters**:

        :subinterface_index: int - The index number of the subinterface -- used to address the logical interface
        :description: str - A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.
        :subinterface_enabled: bool - This leaf contains the configured, desired state of the interface.  Systems that implement the IF-MIB use the value of this leaf in the 'running' datastore to set IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry has been initialized, as described in RFC 2863.  Changes in this leaf in the 'running' datastore are reflected in ifAdminStatus, but if ifAdminStatus is changed over SNMP, this leaf is not affected.
        :address_ip: str - 
        :address_prefix_length: int - 
        :ipv4_enabled: bool - 
        :ipv4_dhcp_client: bool - 
        :ipv6_enabled: bool - 
        :ipv6_dhcp_client: bool - 
    """

    type = kwargs.get('type', None)
    description = kwargs.get('description', None)
    subinterface_enabled = kwargs.get('subinterface_enabled', None)
    address_prefix_length = kwargs.get('address_prefix_length', None)
    ipv4_enabled = kwargs.get('ipv4_enabled', None)
    ipv4_dhcp_client = kwargs.get('ipv4_dhcp_client', None)
    ipv6_enabled = kwargs.get('ipv6_enabled', None)
    ipv6_dhcp_client = kwargs.get('ipv6_dhcp_client', None)

    object_name = 'LO-MGMT'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": "LO-MGMT",
                    "config": {
                        "name": "LO-MGMT",
                        "type": type
                    },
                    "subinterfaces": {
                        "subinterface": [
                            {
                                "index": subinterface_index,
                                "config": {
                                    "index": subinterface_index,
                                    "description": description,
                                    "enabled": subinterface_enabled
                                },
                                "ipv4": {
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    },
                                    "config": {
                                        "enabled": ipv4_enabled,
                                        "dhcp-client": ipv4_dhcp_client
                                    }
                                },
                                "ipv6": {
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    },
                                    "config": {
                                        "enabled": ipv6_enabled,
                                        "dhcp-client": ipv6_dhcp_client
                                    }
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_lo_mgmt(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    """

    object_name = 'LO-MGMT'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_lo_mgmt(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    """

    object_name = 'LO-MGMT'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name,
                    "@operation": "delete"
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def update_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.
    :type type: str

    **Optional Parameters**:

        :interface_name: str - References the name of the interface
        :mtu: int - Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default -- e.g., 1514 bytes on an Ethernet interface.
        :subinterface_index: int - The index number of the subinterface -- used to address the logical interface
        :description: str - A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.
    :type type: str

    **Optional Parameters**:

        :interface_name: str - References the name of the interface
        :mtu: int - Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default -- e.g., 1514 bytes on an Ethernet interface.
        :subinterface_index: int - The index number of the subinterface -- used to address the logical interface
        :description: str - A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.
    """

    type = kwargs.get('type', None)
    mtu = kwargs.get('mtu', None)
    description = kwargs.get('description', None)

    object_name = 'Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name,
                    "config": {
                        "name": interface_name,
                        "type": type,
                        "mtu": mtu
                    },
                    "subinterfaces": {
                        "subinterface": [
                            {
                                "index": subinterface_index,
                                "config": {
                                    "index": subinterface_index,
                                    "description": description
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    """

    object_name = 'Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_ethernet_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.
    :type type: str

    **Optional Parameters**:

        :interface_name: str - References the name of the interface
    :param handle: gxctrl connection handle
    :type handle: str
    :param type: The type of the interface.  When an interface entry is created, a server MAY initialize the type leaf with a valid value, e.g., if it is possible to derive the type from the name of the interface.  If a client tries to set the type of an interface to a value that can never be used by the system, e.g., if the type is not supported or if the type does not match the name of the interface, the server MUST reject the request. A NETCONF server MUST reply with an rpc-error with the error-tag 'invalid-value' in this case.
    :type type: str

    **Optional Parameters**:

        :interface_name: str - References the name of the interface
    """

    type = kwargs.get('type', None)

    object_name = 'Ethernet-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name,
                    "config": {
                        "name": interface_name,
                        "type": type
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_ethernet_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    """

    object_name = 'Ethernet-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_aux_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str

    **Optional Parameters**:

        :mtu: int - Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default -- e.g., 1514 bytes on an Ethernet interface.
        :subinterface_index: int - The index number of the subinterface -- used to address the logical interface
        :description: str - A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.
        :ipv4_enabled: bool - 
        :ipv4_dhcp_client: bool - 
        :address_ip: str - 
        :address_prefix_length: int - 
        :ipv6_enabled: bool - 
        :ipv6_dhcp_client: bool - 
        :auto_negotiate: bool - 
    """

    mtu = kwargs.get('mtu', None)
    description = kwargs.get('description', None)
    ipv4_enabled = kwargs.get('ipv4_enabled', None)
    ipv4_dhcp_client = kwargs.get('ipv4_dhcp_client', None)
    address_ip = kwargs.get('address_ip', None)
    address_prefix_length = kwargs.get('address_prefix_length', None)
    ipv6_enabled = kwargs.get('ipv6_enabled', None)
    ipv6_dhcp_client = kwargs.get('ipv6_dhcp_client', None)
    auto_negotiate = kwargs.get('auto_negotiate', None)

    object_name = 'AUX-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name,
                    "config": {
                        "name": interface_name,
                        "type": "ethernetCsmacd",
                        "mtu": mtu
                    },
                    "subinterfaces": {
                        "subinterface": [
                            {
                                "index": subinterface_index,
                                "config": {
                                    "index": subinterface_index,
                                    "description": description
                                },
                                "ipv4": {
                                    "config": {
                                        "enabled": ipv4_enabled,
                                        "dhcp-client": ipv4_dhcp_client
                                    },
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    }
                                },
                                "ipv6": {
                                    "config": {
                                        "enabled": ipv6_enabled,
                                        "dhcp-client": ipv6_dhcp_client
                                    },
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "ethernet": {
                        "config": {
                            "auto-negotiate": auto_negotiate
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_aux_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    """

    object_name = 'AUX-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_dcn_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str

    **Optional Parameters**:

        :mtu: int - Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default -- e.g., 1514 bytes on an Ethernet interface.
        :subinterface_index: int - The index number of the subinterface -- used to address the logical interface
        :description: str - A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.
        :ipv4_enabled: bool - 
        :ipv4_dhcp_client: bool - 
        :address_ip: str - 
        :address_prefix_length: int - 
        :ipv6_enabled: bool - 
        :ipv6_dhcp_client: bool - 
        :auto_negotiate: bool - 
    """

    mtu = kwargs.get('mtu', None)
    description = kwargs.get('description', None)
    ipv4_enabled = kwargs.get('ipv4_enabled', None)
    ipv4_dhcp_client = kwargs.get('ipv4_dhcp_client', None)
    address_ip = kwargs.get('address_ip', None)
    address_prefix_length = kwargs.get('address_prefix_length', None)
    ipv6_enabled = kwargs.get('ipv6_enabled', None)
    ipv6_dhcp_client = kwargs.get('ipv6_dhcp_client', None)
    auto_negotiate = kwargs.get('auto_negotiate', None)

    object_name = 'DCN-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name,
                    "config": {
                        "name": interface_name,
                        "type": "dcn",
                        "mtu": mtu
                    },
                    "subinterfaces": {
                        "subinterface": [
                            {
                                "index": subinterface_index,
                                "config": {
                                    "index": subinterface_index,
                                    "description": description
                                },
                                "ipv4": {
                                    "config": {
                                        "enabled": ipv4_enabled,
                                        "dhcp-client": ipv4_dhcp_client
                                    },
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    }
                                },
                                "ipv6": {
                                    "config": {
                                        "enabled": ipv6_enabled,
                                        "dhcp-client": ipv6_dhcp_client
                                    },
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "ethernet": {
                        "config": {
                            "auto-negotiate": auto_negotiate
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_dcn_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    """

    object_name = 'DCN-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def update_craft_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str

    **Optional Parameters**:

        :mtu: int - Set the max transmission unit size in octets for the physical interface.  If this is not set, the mtu is set to the operational default -- e.g., 1514 bytes on an Ethernet interface.
        :subinterface_index: int - The index number of the subinterface -- used to address the logical interface
        :description: str - A textual description of the interface.  A server implementation MAY map this leaf to the ifAlias MIB object.  Such an implementation needs to use some mechanism to handle the differences in size and characters allowed between this leaf and ifAlias.  The definition of such a mechanism is outside the scope of this document.  Since ifAlias is defined to be stored in non-volatile storage, the MIB implementation MUST map ifAlias to the value of 'description' in the persistently stored datastore.  Specifically, if the device supports ':startup', when ifAlias is read the device MUST return the value of 'description' in the 'startup' datastore, and when it is written, it MUST be written to the 'running' and 'startup' datastores.  Note that it is up to the implementation to  decide whether to modify this single leaf in 'startup' or perform an implicit copy-config from 'running' to 'startup'.  If the device does not support ':startup', ifAlias MUST be mapped to the 'description' leaf in the 'running' datastore.
        :ipv4_enabled: bool - 
        :ipv4_dhcp_client: bool - 
        :address_ip: str - 
        :address_prefix_length: int - 
        :ipv6_enabled: bool - 
        :ipv6_dhcp_client: bool - 
        :auto_negotiate: bool - 
    """

    mtu = kwargs.get('mtu', None)
    description = kwargs.get('description', None)
    ipv4_enabled = kwargs.get('ipv4_enabled', None)
    ipv4_dhcp_client = kwargs.get('ipv4_dhcp_client', None)
    address_ip = kwargs.get('address_ip', None)
    address_prefix_length = kwargs.get('address_prefix_length', None)
    ipv6_enabled = kwargs.get('ipv6_enabled', None)
    ipv6_dhcp_client = kwargs.get('ipv6_dhcp_client', None)
    auto_negotiate = kwargs.get('auto_negotiate', None)

    object_name = 'CRAFT-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name,
                    "config": {
                        "name": interface_name,
                        "type": "ethernetCsmacd",
                        "mtu": mtu
                    },
                    "subinterfaces": {
                        "subinterface": [
                            {
                                "index": subinterface_index,
                                "config": {
                                    "index": subinterface_index,
                                    "description": description
                                },
                                "ipv4": {
                                    "config": {
                                        "enabled": ipv4_enabled,
                                        "dhcp-client": ipv4_dhcp_client
                                    },
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    }
                                },
                                "ipv6": {
                                    "config": {
                                        "enabled": ipv6_enabled,
                                        "dhcp-client": ipv6_dhcp_client
                                    },
                                    "addresses": {
                                        "address": [
                                            {
                                                "ip": address_ip,
                                                "config": {
                                                    "ip": address_ip,
                                                    "prefix-length": address_prefix_length
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "ethernet": {
                        "config": {
                            "auto-negotiate": auto_negotiate
                        }
                    }
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_craft_interface(handle, interface_name, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param interface_name: References the name of the interface
    :type interface_name: str
    """

    object_name = 'CRAFT-Interface'
    manager = kwargs.get('manager')

    request = {
        "interfaces": {
            "interface": [
                {
                    "name": interface_name
                }
            ]
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def create_dial_out_server(handle, destination_group_group_id, destination_destination_address, destination_destination_port, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param destination_group_group_id: Unique identifier for the destination group
    :type destination_group_group_id: str
    :param destination_destination_address: IP address of the telemetry stream destination
    :type destination_destination_address: str
    :param destination_destination_port: Protocol (udp or tcp) port number for the telemetry stream destination
    :type destination_destination_port: int

    **Optional Parameters**:

        :protocol: str - Dial-out-server session type.
        :retry_policy: str - Retry policy after a timeout.
        :retry: int - Number of retries before giving up.
        :timeout: int - Wait time until timeout.
        :auto_connect: bool - If true, automatically tries to connect to this dial-out-server. Note that a server with auto-connect false can still be connected manually via the call-home RPC.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    :param handle: gxctrl connection handle
    :type handle: str
    :param destination_group_group_id: Unique identifier for the destination group
    :type destination_group_group_id: str
    :param destination_destination_address: IP address of the telemetry stream destination
    :type destination_destination_address: str
    :param destination_destination_port: Protocol (udp or tcp) port number for the telemetry stream destination
    :type destination_destination_port: int

    **Optional Parameters**:

        :protocol: str - Dial-out-server session type.
        :retry_policy: str - Retry policy after a timeout.
        :retry: int - Number of retries before giving up.
        :timeout: int - Wait time until timeout.
        :auto_connect: bool - If true, automatically tries to connect to this dial-out-server. Note that a server with auto-connect false can still be connected manually via the call-home RPC.
        :alarm_report_control: str - Controls the reporting of alarms for this particular object.
    """

    protocol = kwargs.get('protocol', None)
    retry_policy = kwargs.get('retry_policy', None)
    retry = kwargs.get('retry', None)
    timeout = kwargs.get('timeout', None)
    auto_connect = kwargs.get('auto_connect', None)
    alarm_report_control = kwargs.get('alarm_report_control', None)

    object_name = 'Dial-Out-Server'
    manager = kwargs.get('manager')

    request = {
        "telemetry-system": {
            "destination-groups": {
                "destination-group": {
                    "group-id": destination_group_group_id,
                    "config": {
                        "group-id": destination_group_group_id
                    },
                    "destinations": {
                        "destination": {
                            "destination-address": destination_destination_address,
                            "destination-port": destination_destination_port,
                            "config": {
                                "destination-address": destination_destination_address,
                                "destination-port": destination_destination_port,
                                "protocol": protocol,
                                "retry-policy": retry_policy,
                                "retry": retry,
                                "timeout": timeout,
                                "auto-connect": auto_connect,
                                "alarm-report-control": alarm_report_control
                            }
                        }
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def get_dial_out_server(handle, destination_group_group_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param destination_group_group_id: Unique identifier for the destination group
    :type destination_group_group_id: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param destination_group_group_id: Unique identifier for the destination group
    :type destination_group_group_id: str
    """

    object_name = 'Dial-Out-Server'
    manager = kwargs.get('manager')

    request = {
        "telemetry-system": {
            "destination-groups": {
                "destination-group": {
                    "group-id": destination_group_group_id
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_dial_out_server(handle, destination_group_group_id, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param destination_group_group_id: Unique identifier for the destination group
    :type destination_group_group_id: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param destination_group_group_id: Unique identifier for the destination group
    :type destination_group_group_id: str
    """

    object_name = 'Dial-Out-Server'
    manager = kwargs.get('manager')

    request = {
        "telemetry-system": {
            "destination-groups": {
                "destination-group": {
                    "group-id": destination_group_group_id,
                    "@operation": "delete"
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response


def create_user(handle, user_username, password, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    :param password: The user password, supplied as cleartext.  The system must hash the value and only store the hashed value.
    :type password: str

    **Optional Parameters**:

        :password_hashed: str - The user password, supplied as a hashed value using the notation described in the definition of the crypt-password-type.
        :ssh_key: str - SSH public key for the user (RSA or DSA)
        :role: str - Role assigned to the user.  The role may be supplied as a string or a role defined by the SYSTEM_DEFINED_ROLES identity.
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    :param password: The user password, supplied as cleartext.  The system must hash the value and only store the hashed value.
    :type password: str

    **Optional Parameters**:

        :password_hashed: str - The user password, supplied as a hashed value using the notation described in the definition of the crypt-password-type.
        :ssh_key: str - SSH public key for the user (RSA or DSA)
        :role: str - Role assigned to the user.  The role may be supplied as a string or a role defined by the SYSTEM_DEFINED_ROLES identity.
    """

    password_hashed = kwargs.get('password_hashed', None)
    ssh_key = kwargs.get('ssh_key', None)
    role = kwargs.get('role', None)

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "authentication": {
                    "users": {
                        "user": [
                            {
                                "username": user_username,
                                "config": {
                                    "username": user_username,
                                    "password": password,
                                    "password-hashed": password_hashed,
                                    "ssh-key": ssh_key,
                                    "role": role
                                }
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'create', request)
    return response


def update_user(handle, user_username, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    :param password: The user password, supplied as cleartext.  The system must hash the value and only store the hashed value.
    :type password: str

    **Optional Parameters**:

        :password_hashed: str - The user password, supplied as a hashed value using the notation described in the definition of the crypt-password-type.
        :ssh_key: str - SSH public key for the user (RSA or DSA)
        :role: str - Role assigned to the user.  The role may be supplied as a string or a role defined by the SYSTEM_DEFINED_ROLES identity.
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    :param password: The user password, supplied as cleartext.  The system must hash the value and only store the hashed value.
    :type password: str

    **Optional Parameters**:

        :password_hashed: str - The user password, supplied as a hashed value using the notation described in the definition of the crypt-password-type.
        :ssh_key: str - SSH public key for the user (RSA or DSA)
        :role: str - Role assigned to the user.  The role may be supplied as a string or a role defined by the SYSTEM_DEFINED_ROLES identity.
    """

    password = kwargs.get('password', None)
    password_hashed = kwargs.get('password_hashed', None)
    ssh_key = kwargs.get('ssh_key', None)
    role = kwargs.get('role', None)

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "authentication": {
                    "users": {
                        "user": [
                            {
                                "username": user_username,
                                "config": {
                                    "username": user_username,
                                    "password": password,
                                    "password-hashed": password_hashed,
                                    "ssh-key": ssh_key,
                                    "role": role
                                }
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'update', request)
    return response


def get_user(handle, user_username, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    """

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "authentication": {
                    "users": {
                        "user": [
                            {
                                "username": user_username
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'get', request)
    return response


def delete_user(handle, user_username, **kwargs):
    """
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    :param handle: gxctrl connection handle
    :type handle: str
    :param user_username: References the configured username for the user
    :type user_username: str
    """

    object_name = 'User'
    manager = kwargs.get('manager')

    request = {
        "system": {
            "aaa": {
                "authentication": {
                    "users": {
                        "user": [
                            {
                                "username": user_username,
                                "@operation": "delete"
                            }
                        ]
                    }
                }
            }
        }
    }

    response = gxutils.send_request(manager, object_name, 'openconfig', 'delete', request)
    return response

