import xrutils
#
# auto-generated pixi build code file
# Build: XR_R1_1
#

def get_alarmList(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of raised alarms
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/alarmList", q_value=q)
    return response


def get_alarms(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of alarm in the system
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/alarms", q_value=q)
    return response


def get_alarms_by_alarmId(handle, alarmId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific dfm alarm data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param alarmId: Index into the DFM alarm list
        :type alarmId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/alarms/{alarmId}", q_value=q)
    return response


def get_ietf_alarms_alarm_list(handle, **kwargs):
    """
    **Summary**
        ::
            Returns ietf.alarms.alarms.alarmList
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ietf-alarms:alarms/alarm-list", q_value=q)
    return response


def get_ietf_alarms_alarm_list_alarm(handle, **kwargs):
    """
    **Summary**
        ::
            Returns ietf.alarms.alarms.alarm
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ietf-alarms:alarms/alarm-list/alarm", q_value=q)
    return response


def get_subscriptions_events(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of event subscriptions
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/subscriptions/events", q_value=q)
    return response


def build_event_subscription_filter(handle, **kwargs):
    """
    **Summary**
        ::
            Helper method for create_subscriptions_events

        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :requestedNotificationTypes: array - Required notification types to be available in the notification channel
            - OC: Object Creation
            - OD: Object Deletion
            - AVC: Attribute Value Change
            - ERROR: Error notifications
            
        :resourceType: string - Required resource types to be available in the notification channel
            Resource types are identified by the 'rt' link in the resource object
             Possible Values: cm.device, cm.host, cm.host.port, cm.module, cm.module.linePtp, cm.module.linePtp.carrier, cm.module.linePtp.carrier.dscg, cm.module.linePtp.carrier.dsc, cm.module.otu, cm.module.otu.odu, cm.module.ethernetClient, cm.module.localConnection, cm.transport-capacity, cm.transport-capacity.endpoint, cm.capacity-link, cm.network-connection, cm.network-connection.endpoint, cm.network-connection.local-connection, cm.xr-network, cm.xr-network.hubModule, cm.xr-network.leafModule, cm.xr-network.reachableModule, cm.sw.action, cm.sw.moduleAction, cm.sw.ctrl, cm.sw.bank, cm.ndu, cm.ndu.port, cm.ndu.port.tom, cm.ndu.port.xr, cm.ndu.port.edfa, cm.ndu.port.voa, cm.ndu.linePtp, cm.ndu.linePtp.carrier, cm.ndu.tribPtp, cm.ndu.polPtp, cm.ndu.otu, cm.ndu.ethernet, cm.ndu.lc, cm.ndu.fanUnit, cm.ndu.pem, cm.ndu.leds
        :ids: array - Required resource ids (with type defined in resourceType) to be available in the notification channel
        :moduleIds: array - Required device ids (di property) within the defined resourceType (i.e. resource type containing the device ids) to be available in the notification channel
        :hrefs: array - Required HREFs to be available in the notification channel.
            Note that this filter definition supports regex.
            
    """
    requestedNotificationTypes = kwargs.get('requestedNotificationTypes', None)
    resourceType = kwargs.get('resourceType', None)
    ids = kwargs.get('ids', None)
    moduleIds = kwargs.get('moduleIds', None)
    hrefs = kwargs.get('hrefs', None)

    data = {
        "requestedNotificationTypes": requestedNotificationTypes,
        "requestedResources": [
            {
                "resourceType": resourceType,
                "ids": ids,
                "moduleIds": moduleIds,
                "hrefs": hrefs
            }
        ]
    }

    return data


def create_subscriptions_events(handle, **kwargs):
    """
    **Summary**
        ::
            Create event Subscriptions
    
        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :subscriptionName: string - User defined subscription name.
        :subscriptionFilters: object - Sourced from build_event_subscription_filter
    """
    subscriptionName = kwargs.get('subscriptionName', None)
    subscriptionFilters = kwargs.get('subscriptionFilters', None)

    request = [
        {
            "subscriptionName": subscriptionName,
            "subscriptionFilters": subscriptionFilters
        }
    ]

    response = xrutils.send_request(handle, "POST", f"/api/v1/subscriptions/events", request_body=request)
    return response


def get_subscriptions_events_by_subscriptionIdx(handle, subscriptionIdx, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific event subscription data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param subscriptionIdx: Index into the Hosts list
        :type subscriptionIdx: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/subscriptions/events/{subscriptionIdx}", q_value=q)
    return response


def update_subscriptions_events(handle, subscriptionIdx, **kwargs):
    """
    **Summary**
        ::
            Update event subscription data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param subscriptionIdx: Index into the Hosts list
        :type subscriptionIdx: string
    
    
    **Optional Parameters**
        :subscriptionName: string - User defined subscription name.
        :subscriptionFilters: object - Sourced from build_event_subscription_filter
    """
    subscriptionName = kwargs.get('subscriptionName', None)
    subscriptionFilters = kwargs.get('subscriptionFilters', None)

    request = {
        "subscriptionName": subscriptionName,
        "subscriptionFilters": subscriptionFilters
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/subscriptions/events/{subscriptionIdx}")
    return response


def delete_subscriptions_events(handle, subscriptionIdx, **kwargs):
    """
    **Summary**
        ::
            Delete event subscription
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param subscriptionIdx: Index into the Hosts list
        :type subscriptionIdx: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/subscriptions/events/{subscriptionIdx}")
    return response


def get_subscriptions_alarms(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of alarm subscriptions
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/subscriptions/alarms", q_value=q)
    return response


def build_alarm_subscription_filter(handle, **kwargs):
    """
    **Summary**
        ::
            Helper method for create_subscriptions_alarms

        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :alarmClearanceStatus: string - Only applicable for alarm-notification events. 
            The clearance status of the alarm.
            Possible values:
              1) 'any':
                - Ignore alarm-clearance status.
              2) 'cleared':
                - Filter cleared alarms.
              3) 'not-cleared':
                - Filter not-cleared alarms.
             Possible Values: any, cleared, not-cleared
        :seconds: integer - Age expressed in seconds.
        :minutes: integer - Age expressed in minutes.
        :hours: integer - Age expressed in hours.
        :days: integer - Age expressed in days.
        :weeks: integer - Age expressed in weeks.
        :below: string - Severity less than this leaf. Possible Values: critical, major, warning, minor, indeterminate
        :is_: string - Severity level equal to this leaf. Possible Values: indeterminate, warning, minor, major, critical
        :above: string - Severity level higher than this leaf. Possible Values: indeterminate, warning, minor, major, critical
        :operatorState: string - Filter on alarm operatorParameters state. Possible Values: none, ack, closed, shelved, un-shelved
        :user: string - Filter based on alarm operatorParameters operator.
    """
    alarmClearanceStatus = kwargs.get('alarmClearanceStatus', None)
    seconds = kwargs.get('seconds', None)
    minutes = kwargs.get('minutes', None)
    hours = kwargs.get('hours', None)
    days = kwargs.get('days', None)
    weeks = kwargs.get('weeks', None)
    below = kwargs.get('below', None)
    is_ = kwargs.get('is_', None)
    above = kwargs.get('above', None)
    operatorState = kwargs.get('operatorState', None)
    user = kwargs.get('user', None)

    data = {
        "alarmClearanceStatus": alarmClearanceStatus,
        "olderThan": {
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days,
            "weeks": weeks
        },
        "severity": {
            "below": below,
            "is": is_,
            "above": above
        },
        "operatorStateFilter": {
            "operatorState": operatorState,
            "user": user
        }
    }

    return data


def create_subscriptions_alarms(handle, **kwargs):
    """
    **Summary**
        ::
            Create alarm Subscriptions
    
        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :subscriptionName: string - User defined subscription name.
        :subscriptionFilters: object - Sourced from build_alarm_subscription_filter
    """
    subscriptionName = kwargs.get('subscriptionName', None)
    subscriptionFilters = kwargs.get('subscriptionFilters', None)

    request = [
        {
            "subscriptionName": subscriptionName,
            "subscriptionFilters": subscriptionFilters
        }
    ]

    response = xrutils.send_request(handle, "POST", f"/api/v1/subscriptions/alarms", request_body=request)
    return response


def get_subscriptions_alarms_by_subscriptionIdx(handle, subscriptionIdx, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific alarm subscription data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param subscriptionIdx: Index into the Hosts list
        :type subscriptionIdx: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/subscriptions/alarms/{subscriptionIdx}", q_value=q)
    return response


def update_subscriptions_alarms(handle, subscriptionIdx, **kwargs):
    """
    **Summary**
        ::
            Update alarm subscription data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param subscriptionIdx: Index into the Hosts list
        :type subscriptionIdx: string
    
    
    **Optional Parameters**
        :subscriptionName: string - User defined subscription name.
        :subscriptionFilters: object - Sourced from build_alarm_subscription_filter
    """
    subscriptionName = kwargs.get('subscriptionName', None)
    subscriptionFilters = kwargs.get('subscriptionFilters', None)

    request = {
        "subscriptionName": subscriptionName,
        "subscriptionFilters": subscriptionFilters
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/subscriptions/alarms/{subscriptionIdx}")
    return response


def delete_subscriptions_alarms(handle, subscriptionIdx, **kwargs):
    """
    **Summary**
        ::
            Delete alarm subscription
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param subscriptionIdx: Index into the Hosts list
        :type subscriptionIdx: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/subscriptions/alarms/{subscriptionIdx}")
    return response


def get_hosts(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all hosts
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/hosts", q_value=q)
    return response


def create_hosts(handle, **kwargs):
    """
    **Summary**
        ::
            Create hosts
    
        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :managedBy: string - Indicates whether orchestration should be done through CM interface or through Host interface
            Possible values: 'host', 'cm'
            - 'host': Managed through host interface and discovered by CM
                      Cannot be edited or deleted through CM interface
            - 'cm': Managed through CM interface
                    Can be edited or deleted through CM interface
             Possible Values: host, cm
        :latitude: number - 
        :longitude: number - 
        :labels: object - Assign key:value labels to objects
        :selector:
            hostSelectorByHostChassisId :
                :chassisIdSubtype: string - Value of chassisIdSubtype (encoding of chassisId) within LLDP data.
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :chassisId: string - Value of chassisId within LLDP data
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
            moduleSelectorByModuleId :
                :moduleId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules using moduleId.
                
            moduleSelectorByModuleName :
                :moduleName: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
            moduleSelectorByModuleMAC :
                :moduleMAC: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
            moduleSelectorByModuleSerialNumber :
                :moduleSerialNumber: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
    """
    name = kwargs.get('name', None)
    managedBy = kwargs.get('managedBy', None)
    latitude = kwargs.get('latitude', None)
    longitude = kwargs.get('longitude', None)
    labels = kwargs.get('labels', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    chassisId = kwargs.get('chassisId', None)
    moduleId = kwargs.get('moduleId', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    moduleName = kwargs.get('moduleName', None)

    request = [
        {
            "name": name,
            "managedBy": managedBy,
            "location": {
                "latitude": latitude,
                "longitude": longitude
            },
            "selector": {
                "hostSelectorByHostChassisId": {
                    "chassisIdSubtype": chassisIdSubtype,
                    "chassisId": chassisId
                },
                "moduleSelectorByModuleId": {
                    "moduleId": moduleId
                },
                "moduleSelectorByModuleName": {
                    "moduleName": moduleName
                },
                "moduleSelectorByModuleMAC": {
                    "moduleMAC": moduleMAC
                },
                "moduleSelectorByModuleSerialNumber": {
                    "moduleSerialNumber": moduleSerialNumber
                }
            },
            "labels": labels
        }
    ]

    request = xrutils.selector_parse(request, selector)
    response = xrutils.send_request(handle, "POST", f"/api/v1/hosts", request_body=request)
    return response


def get_hosts_by_hostId(handle, hostId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific host data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/hosts/{hostId}", q_value=q)
    return response


def update_hosts(handle, hostId, **kwargs):
    """
    **Summary**
        ::
            update host
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
    
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :managedBy: string - Indicates whether orchestration should be done through CM interface or through Host interface
            Possible values: 'host', 'cm'
            - 'host': Managed through host interface and discovered by CM
                      Cannot be edited or deleted through CM interface
            - 'cm': Managed through CM interface
                    Can be edited or deleted through CM interface
             Possible Values: host, cm
        :latitude: number - 
        :longitude: number - 
        :labels: object - Assign key:value labels to objects
    """
    name = kwargs.get('name', None)
    managedBy = kwargs.get('managedBy', None)
    latitude = kwargs.get('latitude', None)
    longitude = kwargs.get('longitude', None)
    labels = kwargs.get('labels', None)

    request = {
        "name": name,
        "managedBy": managedBy,
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "labels": labels
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/hosts/{hostId}")
    return response


def delete_hosts(handle, hostId, **kwargs):
    """
    **Summary**
        ::
            delete specific host
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/hosts/{hostId}")
    return response


def get_hosts_ports(handle, hostId, **kwargs):
    """
    **Summary**
        ::
            Retrieve host' ports
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/hosts/{hostId}/ports", q_value=q)
    return response


def create_hosts_ports(handle, hostId, **kwargs):
    """
    **Summary**
        ::
            Create host ports
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
    
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :managedBy: string - Indicates whether orchestration should be done through CM interface or through Host interface
            Possible values: 'host', 'cm'
            - 'host': Managed through host interface and discovered by CM
                      Cannot be edited or deleted through CM interface
            - 'cm': Managed through CM interface
                    Can be edited or deleted through CM interface
             Possible Values: host, cm
        :labels: object - Assign key:value labels to objects
        :selector:
            hostPortSelectorByName :
                :hostName: string - User defined host name.
                
                :hostPortName: string - User defined host port name.
                
            hostPortSelectorByPortId :
                :chassisIdSubtype: string - Value of chassisIdSubtype (encoding of chassisId) within LLDP data.
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :chassisId: string - Value of chassisId within LLDP data
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :portIdSubtype: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
                :portId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
            hostPortSelectorBySysName :
                :sysName: string - Value of System Name within LLDP data
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :portIdSubtype: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
                :portId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
            hostPortSelectorByPortSourceMAC :
                :portSourceMAC: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the portSourceMAC.
                
            moduleIfSelectorByModuleId :
                :moduleId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules using moduleId.
                
                :moduleClientIfAid: string - TODO
                
            moduleIfSelectorByModuleName :
                :moduleName: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :moduleClientIfAid: string - TODO
                
            moduleIfSelectorByModuleMAC :
                :moduleMAC: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :moduleClientIfAid: string - TODO
                
            moduleIfSelectorByModuleSerialNumber :
                :moduleSerialNumber: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :moduleClientIfAid: string - TODO
                
    """
    name = kwargs.get('name', None)
    managedBy = kwargs.get('managedBy', None)
    labels = kwargs.get('labels', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    hostPortName = kwargs.get('hostPortName', None)
    chassisId = kwargs.get('chassisId', None)
    portSourceMAC = kwargs.get('portSourceMAC', None)
    moduleName = kwargs.get('moduleName', None)
    moduleClientIfAid = kwargs.get('moduleClientIfAid', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    moduleId = kwargs.get('moduleId', None)
    portId = kwargs.get('portId', None)
    portIdSubtype = kwargs.get('portIdSubtype', None)
    sysName = kwargs.get('sysName', None)
    hostName = kwargs.get('hostName', None)

    request = [
        {
            "name": name,
            "managedBy": managedBy,
            "selector": {
                "hostPortSelectorByName": {
                    "hostName": hostName,
                    "hostPortName": hostPortName
                },
                "hostPortSelectorByPortId": {
                    "chassisIdSubtype": chassisIdSubtype,
                    "chassisId": chassisId,
                    "portIdSubtype": portIdSubtype,
                    "portId": portId
                },
                "hostPortSelectorBySysName": {
                    "sysName": sysName,
                    "portIdSubtype": portIdSubtype,
                    "portId": portId
                },
                "hostPortSelectorByPortSourceMAC": {
                    "portSourceMAC": portSourceMAC
                },
                "moduleIfSelectorByModuleId": {
                    "moduleId": moduleId,
                    "moduleClientIfAid": moduleClientIfAid
                },
                "moduleIfSelectorByModuleName": {
                    "moduleName": moduleName,
                    "moduleClientIfAid": moduleClientIfAid
                },
                "moduleIfSelectorByModuleMAC": {
                    "moduleMAC": moduleMAC,
                    "moduleClientIfAid": moduleClientIfAid
                },
                "moduleIfSelectorByModuleSerialNumber": {
                    "moduleSerialNumber": moduleSerialNumber,
                    "moduleClientIfAid": moduleClientIfAid
                }
            },
            "labels": labels
        }
    ]

    request = xrutils.selector_parse(request, selector)
    response = xrutils.send_request(handle, "POST", f"/api/v1/hosts/{hostId}/ports", request_body=request)
    return response


def get_hosts_ports_by_portIdx(handle, hostId, portIdx, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific host's port
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
        :param portIdx: Index into the Ports list
        :type portIdx: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/hosts/{hostId}/ports/{portIdx}", q_value=q)
    return response


def update_hosts_ports(handle, hostId, portIdx, **kwargs):
    """
    **Summary**
        ::
            update hosts' Port
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
        :param portIdx: Index into the Ports list
        :type portIdx: string
    
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :managedBy: string - Indicates whether orchestration should be done through CM interface or through Host interface
            Possible values: 'host', 'cm'
            - 'host': Managed through host interface and discovered by CM
                      Cannot be edited or deleted through CM interface
            - 'cm': Managed through CM interface
                    Can be edited or deleted through CM interface
             Possible Values: host, cm
        :labels: object - Assign key:value labels to objects
    """
    name = kwargs.get('name', None)
    managedBy = kwargs.get('managedBy', None)
    labels = kwargs.get('labels', None)

    request = {
        "name": name,
        "managedBy": managedBy,
        "labels": labels
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/hosts/{hostId}/ports/{portIdx}")
    return response


def delete_hosts_ports(handle, hostId, portIdx, **kwargs):
    """
    **Summary**
        ::
            delete specific host port
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param hostId: Index into the Hosts list
        :type hostId: string
        :param portIdx: Index into the Ports list
        :type portIdx: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/hosts/{hostId}/ports/{portIdx}")
    return response


def get_modules(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all modules
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules", q_value=q)
    return response


def get_modules_by_moduleId(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}", q_value=q)
    return response


def update_modules(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Update module data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    
    **Optional Parameters**
        :moduleName: string - Property to change the device name. This is also reflected in the same property in oic.wk.d
        :labels: object - Assign key:value labels to objects
    """
    moduleName = kwargs.get('moduleName', None)
    labels = kwargs.get('labels', None)

    request = {
        "moduleName": moduleName,
        "labels": labels
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/modules/{moduleId}")
    return response


def delete_modules(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Delete specific module
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/modules/{moduleId}")
    return response


def perform_modules_coldStart(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Cold Start operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/modules/{moduleId}/coldStart", request_body=request)
    return response


def perform_modules_warmStart(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Warm Start operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/modules/{moduleId}/warmStart", request_body=request)
    return response


def perform_modules_factoryReset(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Factory reset operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/modules/{moduleId}/factoryReset", request_body=request)
    return response


def get_modules_linePtps(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all module line ports
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps", q_value=q)
    return response


def get_modules_linePtps_by_linePtpColId(handle, moduleId, linePtpColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module line port data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}", q_value=q)
    return response


def get_modules_ethernetClients(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all module client ethernet interfaces
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/ethernetClients", q_value=q)
    return response


def get_modules_ethernetClients_by_ethernetColId(handle, moduleId, ethernetColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific client ethernet interface data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param ethernetColId: Ethernet client signal identifier within module.
        :type ethernetColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/ethernetClients/{ethernetColId}", q_value=q)
    return response


def update_modules_ethernetClients(handle, moduleId, ethernetColId, **kwargs):
    """
    **Summary**
        ::
            Update module client ethernet interface data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param ethernetColId: Ethernet client signal identifier within module.
        :type ethernetColId: integer
    
    
    **Optional Parameters**
        :fecMode: string - Forward error correction mode of operation Possible Values: enabled, disabled
        :termLB: string - Post-FEC terminal loopback mode for the ethernet client.
            Loopback type:
            - disabled
            - loopback            - Signal is looped back and LF maintenance signal is sent downstream.
            - loopbackAndContinue - Signal is looped back and is also forwarded downstream.
             Possible Values: disabled, loopback, loopbackAndContinue
        :termLBDuration: integer - Duration of the terminal loopback configuration in seconds.
            After the specified time, module automatically disables the terminal loopback.
            0 value is used for indefinitely.
            
        :termTestSignalGen: string - Allows selection of test signal type for generation towards network direction.
            Possible values:
              * 'disabled':       Used when no test signal insertion is required.
              * 'scrambledIdle':  Insert PCS Idle towards towards network direction.
             Possible Values: disabled, scrambledIdle
        :adminStatus: string - Administrative state to Enable/Disable LLDP in rxOnly mode. Possible Values: rxOnly, disabled
        :gccFwd: boolean - Enable/Disable forwarding of untagged LLDP frames over GCC.
              * `true`  - Enabled.
              * `false` - Disabled.
            
        :hostRxDrop: boolean - Enable/Disable LLDP drop in Rx direction of Ethernet Client ports.
              * `true`:  - Enabled.
              * `false`: - Disabled.
            
        :TTLUsage: boolean - Enable/Disable usage of TTL values for flushing/starting LLDP internal flush timer.
              * `true`:  - Enabled.
              * `false`: - Disabled.
            
    """
    fecMode = kwargs.get('fecMode', None)
    termLB = kwargs.get('termLB', None)
    termLBDuration = kwargs.get('termLBDuration', None)
    termTestSignalGen = kwargs.get('termTestSignalGen', None)
    adminStatus = kwargs.get('adminStatus', None)
    gccFwd = kwargs.get('gccFwd', None)
    hostRxDrop = kwargs.get('hostRxDrop', None)
    TTLUsage = kwargs.get('TTLUsage', None)

    request = {
        "fecMode": fecMode,
        "diagnostics": {
            "termLB": termLB,
            "termLBDuration": termLBDuration,
            "termTestSignalGen": termTestSignalGen
        },
        "lldp": {
            "adminStatus": adminStatus,
            "gccFwd": gccFwd,
            "hostRxDrop": hostRxDrop,
            "TTLUsage": TTLUsage
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/modules/{moduleId}/ethernetClients/{ethernetColId}")
    return response


def perform_modules_ethernetClients_clrLldpStats(handle, moduleId, ethernetColId, **kwargs):
    """
    **Summary**
        ::
            Clear LLDP statistics operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param ethernetColId: Ethernet client signal identifier within module.
        :type ethernetColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/modules/{moduleId}/ethernetClients/{ethernetColId}/clrLldpStats", request_body=request)
    return response


def perform_modules_ethernetClients_flushLldpHostDb(handle, moduleId, ethernetColId, **kwargs):
    """
    **Summary**
        ::
            Flush LLDP database operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param ethernetColId: Ethernet client signal identifier within module.
        :type ethernetColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/modules/{moduleId}/ethernetClients/{ethernetColId}/flushLldpHostDb", request_body=request)
    return response


def get_modules_ethernetClients_acs(handle, moduleId, ethernetColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all attachment circuits of a module client ethernet interface
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param ethernetColId: Ethernet client signal identifier within module.
        :type ethernetColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/ethernetClients/{ethernetColId}/acs", q_value=q)
    return response


def get_modules_ethernetClients_acs_by_acColId(handle, moduleId, ethernetColId, acColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific client ethernet attachment circuit data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param ethernetColId: Ethernet client signal identifier within module.
        :type ethernetColId: integer
        :param acColId: attachment circuit identifier within module client ethernet interface.
        :type acColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/ethernetClients/{ethernetColId}/acs/{acColId}", q_value=q)
    return response


def get_modules_localConnections(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all module localConnections
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/localConnections", q_value=q)
    return response


def get_modules_localConnections_by_lcColId(handle, moduleId, lcColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module local connection data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param lcColId: local connection identifier within module.
        :type lcColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/localConnections/{lcColId}", q_value=q)
    return response


def get_modules_otus(handle, moduleId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all module OTUs
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/otus", q_value=q)
    return response


def get_modules_otus_by_otuColId(handle, moduleId, otuColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module OTU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param otuColId: OTU signal identifier within module.
        :type otuColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/otus/{otuColId}", q_value=q)
    return response


def update_modules_otus(handle, moduleId, otuColId, **kwargs):
    """
    **Summary**
        ::
            Update module OTU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param otuColId: OTU signal identifier within module.
        :type otuColId: integer
    
    
    **Optional Parameters**
        :termLB: string - Enable/Disable terminal loopback.
            Loopback type:
              - 'disabled'
              - 'loopback':             Signal is looped back and LF maintenance signal is sent downstream.
             Possible Values: disabled, loopback
        :termLBDuration: integer - Duration of the terminal loopback configuration in seconds.
            After the specified time, module automatically disables the terminal loopback.
            Value '0' is used for indefinitely.
            
    """
    termLB = kwargs.get('termLB', None)
    termLBDuration = kwargs.get('termLBDuration', None)

    request = {
        "diagnostics": {
            "termLB": termLB,
            "termLBDuration": termLBDuration
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/modules/{moduleId}/otus/{otuColId}")
    return response


def get_modules_otus_odus(handle, moduleId, otuColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all module ODUs
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param otuColId: OTU signal identifier within module.
        :type otuColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/otus/{otuColId}/odus", q_value=q)
    return response


def get_modules_otus_odus_by_oduColId(handle, moduleId, otuColId, oduColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module ODU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param otuColId: OTU signal identifier within module.
        :type otuColId: integer
        :param oduColId: ODU signal identifier within module.
        :type oduColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/otus/{otuColId}/odus/{oduColId}", q_value=q)
    return response


def update_modules_otus_odus(handle, moduleId, otuColId, oduColId, **kwargs):
    """
    **Summary**
        ::
            Update module ODU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param otuColId: OTU signal identifier within module.
        :type otuColId: integer
        :param oduColId: ODU signal identifier within module.
        :type oduColId: integer
    
    
    **Optional Parameters**
        :facPRBSGen: boolean - Enable/Disable facility PRBS test pattern generation
        :facPRBSMon: boolean - Enable/Disable facility PRBS test pattern monitoring
    """
    facPRBSGen = kwargs.get('facPRBSGen', None)
    facPRBSMon = kwargs.get('facPRBSMon', None)

    request = {
        "diagnostics": {
            "facPRBSGen": facPRBSGen,
            "facPRBSMon": facPRBSMon
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/modules/{moduleId}/otus/{otuColId}/odus/{oduColId}")
    return response


def get_modules_linePtps_carriers(handle, moduleId, linePtpColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all module carriers
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers", q_value=q)
    return response


def get_modules_linePtps_carriers_by_carrierColId(handle, moduleId, linePtpColId, carrierColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module carrier data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
        :param carrierColId: Carrier identifier within module line port.
        :type carrierColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers/{carrierColId}", q_value=q)
    return response


def update_modules_linePtps_carriers(handle, moduleId, linePtpColId, carrierColId, **kwargs):
    """
    **Summary**
        ::
            Update module Carrier data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
        :param carrierColId: Carrier identifier within module line port.
        :type carrierColId: integer
    
    
    **Optional Parameters**
        :termLB: string - Enable/Disable terminal loopback.
            Loopback type:
            - 'disabled'
            - 'loopbackAndContinue': Signal is looped back and is also forwarded downstream.
             Possible Values: disabled, loopbackAndContinue
        :termLBDuration: integer - Duration of the terminal loopback configuration in seconds.
            After the specified time, module automatically disables the terminal loopback.
            0 value is used for indefinitely.
            
    """
    termLB = kwargs.get('termLB', None)
    termLBDuration = kwargs.get('termLBDuration', None)

    request = {
        "diagnostics": {
            "termLB": termLB,
            "termLBDuration": termLBDuration
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers/{carrierColId}")
    return response


def get_modules_linePtps_carriers_dscgs(handle, moduleId, linePtpColId, carrierColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all module Dscgs
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
        :param carrierColId: Carrier identifier within module line port.
        :type carrierColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers/{carrierColId}/dscgs", q_value=q)
    return response


def get_modules_linePtps_carriers_dscgs_by_dscgColId(handle, moduleId, linePtpColId, carrierColId, dscgColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module dscg data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
        :param carrierColId: Carrier identifier within module line port.
        :type carrierColId: integer
        :param dscgColId: DSCG identifier within module carrier.
        :type dscgColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers/{carrierColId}/dscgs/{dscgColId}", q_value=q)
    return response


def get_modules_linePtps_carriers_dscs(handle, moduleId, linePtpColId, carrierColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all carrier dscs
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
        :param carrierColId: Carrier identifier within module line port.
        :type carrierColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers/{carrierColId}/dscs", q_value=q)
    return response


def get_modules_linePtps_carriers_dscs_by_dscColId(handle, moduleId, linePtpColId, carrierColId, dscColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific carrier dsc data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
        :param carrierColId: Carrier identifier within module line port.
        :type carrierColId: integer
        :param dscColId: DSC identifier within module carrier.
        :type dscColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers/{carrierColId}/dscs/{dscColId}", q_value=q)
    return response


def update_modules_linePtps_carriers_dscs(handle, moduleId, linePtpColId, carrierColId, dscColId, **kwargs):
    """
    **Summary**
        ::
            Update carrier DSC data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param linePtpColId: Line port identifier within module.
        :type linePtpColId: integer
        :param carrierColId: Carrier identifier within module line port.
        :type carrierColId: integer
        :param dscColId: DSC identifier within module carrier.
        :type dscColId: integer
    
    
    **Optional Parameters**
        :relativeDPO: integer - Relative Power offset in hundreds of dB relative to the average DSC power.
        :facPRBSGen: boolean - Enable/Disable facility PRBS test pattern generation
        :facPRBSMon: boolean - Enable/Disable facility PRBS test pattern monitoring
    """
    relativeDPO = kwargs.get('relativeDPO', None)
    facPRBSGen = kwargs.get('facPRBSGen', None)
    facPRBSMon = kwargs.get('facPRBSMon', None)

    request = {
        "relativeDPO": relativeDPO,
        "diagnostics": {
            "facPRBSGen": facPRBSGen,
            "facPRBSMon": facPRBSMon
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/modules/{moduleId}/linePtps/{linePtpColId}/carriers/{carrierColId}/dscs/{dscColId}")
    return response


def get_modules_resources_by_resourceAid(handle, moduleId, resourceAid, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific resource data by AID
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleId: Module identifier.
        :type moduleId: string
        :param resourceAid: resource access identifier.
        :type resourceAid: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/modules/{moduleId}/resources/{resourceAid}", q_value=q)
    return response


def get_network_connections(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all network connections
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/network-connections", q_value=q)
    return response


def build_nc_endpoint(handle, **kwargs):
    """
    **Summary**
        ::
            Helper method for create_network_connections

        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :capacity: integer - Client to network capacity of the attachment circuit.
            Possible values are defined in multiples of 25Gbps up to maximum module rate.
            
    **Selector**
        :param selector: - 
            hostPortSelectorByName :
                hostName - string - User defined host name.
                hostPortName - string - User defined host port name.
            hostPortSelectorByPortId :
                chassisIdSubtype - string - Value of chassisIdSubtype (encoding of 
                    chassisId) within LLDP data. Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
                chassisId - string - Value of chassisId within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorBySysName :
                sysName - string - Value of System Name within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorByPortSourceMAC :
                portSourceMAC - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    portSourceMAC.
            moduleIfSelectorByModuleId :
                moduleId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules using moduleId.
                moduleClientIfAid - string - TODO
            moduleIfSelectorByModuleName :
                moduleName - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
                moduleClientIfAid - string - TODO
            moduleIfSelectorByModuleMAC :
                moduleMAC - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
                moduleClientIfAid - string - TODO
            moduleIfSelectorByModuleSerialNumber :
                moduleSerialNumber - string - Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
                moduleClientIfAid - string - TODO
    """
    capacity = kwargs.get('capacity', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    hostPortName = kwargs.get('hostPortName', None)
    chassisId = kwargs.get('chassisId', None)
    portSourceMAC = kwargs.get('portSourceMAC', None)
    moduleName = kwargs.get('moduleName', None)
    moduleClientIfAid = kwargs.get('moduleClientIfAid', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    moduleId = kwargs.get('moduleId', None)
    portId = kwargs.get('portId', None)
    portIdSubtype = kwargs.get('portIdSubtype', None)
    sysName = kwargs.get('sysName', None)
    hostName = kwargs.get('hostName', None)

    data = {
        "selector": {
            "hostPortSelectorByName": {
                "hostName": hostName,
                "hostPortName": hostPortName
            },
            "hostPortSelectorByPortId": {
                "chassisIdSubtype": chassisIdSubtype,
                "chassisId": chassisId,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorBySysName": {
                "sysName": sysName,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorByPortSourceMAC": {
                "portSourceMAC": portSourceMAC
            },
            "moduleIfSelectorByModuleId": {
                "moduleId": moduleId,
                "moduleClientIfAid": moduleClientIfAid
            },
            "moduleIfSelectorByModuleName": {
                "moduleName": moduleName,
                "moduleClientIfAid": moduleClientIfAid
            },
            "moduleIfSelectorByModuleMAC": {
                "moduleMAC": moduleMAC,
                "moduleClientIfAid": moduleClientIfAid
            },
            "moduleIfSelectorByModuleSerialNumber": {
                "moduleSerialNumber": moduleSerialNumber,
                "moduleClientIfAid": moduleClientIfAid
            }
        },
        "capacity": capacity
    }

    data = xrutils.selector_parse(data, selector)
    return data


def create_network_connections(handle, **kwargs):
    """
    **Summary**
        ::
            Create network connections
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param serviceMode: Provides the network connection type.
            Possible values:
            - 'XR-L1': Provides transparent service of Ethernet or OTN traffic between XR hub and leaf client ports
            - 'XR-VTI-P2P': Provides VTI service between XR hub and leaf client ports
             Possible Values: XR-L1, XR-VTI-P2P
        :type serviceMode: string
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :mc: string - Match criteria applied to the packets received from network side before sending to the client side.
            Possible Values:
            - 'matchAll': All packets from the associated client interface
            - 'matchOuterVID': Based on outer VLAN ID
            - 'none'
            
        :outerVID: string - String format listing of one or more individual VLAN IDs separated by "&" and/or ranges of VLAN IDs connected with "&&". 
            Example "10,20,50..100" represents the VLAN IDs 10, 20 and the vlan range from 50 to 100.
            
        :implicitTransportCapacity: string - This parameter specifies whether the server transport-capacity can be implicitly created/deleted as a result of a network-connection creation/deletion.
            On network-connection creation, if set to 'none' and no transport-capacity exists, creation request will be rejected.
            On network-connection creation, if set to a value other than 'none' and no transport-capacity exists, it shall be automatically created with the corresponding capacityMode.
            On network-connection deletion, if set to a value other than 'none', the supporting transport-capacity will be deleted.
            Depending on the requested service mode, the network-connection request with implicit transport-capacity creation may require additional parameters (e.g., endpoint capacity).
            If set to a value other than 'none' and the corresponding transport-capacity already exists, the transport-capacity capacityMode and endpoint capacity values must match the implicitTransportCapacity and endpoint capacity values in the network-connection request. 
            Otherwise, service creation is rejected.
             Possible Values: none, portMode, dedicatedDownlinkSymmetric, dedicatedDownlinkAsymmetric, sharedDownlink
        :labels: object - Assign key:value labels to objects
        :epA: object - Sourced from build_nc_endpoint
        :epZ: object - Sourced from build_nc_endpoint
    """
    name = kwargs.get('name', None)
    serviceMode = kwargs.get('serviceMode', None)
    mc = kwargs.get('mc', None)
    outerVID = kwargs.get('outerVID', None)
    implicitTransportCapacity = kwargs.get('implicitTransportCapacity', None)
    labels = kwargs.get('labels', None)
    epA = kwargs.get('epA', None)
    epZ = kwargs.get('epZ', None)

    request = [
        {
            "name": name,
            "serviceMode": serviceMode,
            "mc": mc,
            "outerVID": outerVID,
            "implicitTransportCapacity": implicitTransportCapacity,
            "labels": labels,
            "endpoints": [
                epA,
                epZ
            ]
        }
    ]

    response = xrutils.send_request(handle, "POST", f"/api/v1/network-connections", request_body=request)
    return response


def get_network_connections_by_ncId(handle, ncId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific network connection data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/network-connections/{ncId}", q_value=q)
    return response


def update_network_connections(handle, ncId, **kwargs):
    """
    **Summary**
        ::
            Update specific network connection data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
    
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :serviceMode: string - Provides the network connection type.
            Possible values:
            - 'XR-L1': Provides transparent service of Ethernet or OTN traffic between XR hub and leaf client ports
            - 'XR-VTI-P2P': Provides VTI service between XR hub and leaf client ports
             Possible Values: XR-L1, XR-VTI-P2P
        :mc: string - Match criteria applied to the packets received from network side before sending to the client side.
            Possible Values:
            - 'matchAll': All packets from the associated client interface
            - 'matchOuterVID': Based on outer VLAN ID
            - 'none'
            
        :outerVID: string - String format listing of one or more individual VLAN IDs separated by "&" and/or ranges of VLAN IDs connected with "&&". 
            Example "10,20,50..100" represents the VLAN IDs 10, 20 and the vlan range from 50 to 100.
            
        :implicitTransportCapacity: string - This parameter specifies whether the server transport-capacity can be implicitly created/deleted as a result of a network-connection creation/deletion.
            On network-connection creation, if set to 'none' and no transport-capacity exists, creation request will be rejected.
            On network-connection creation, if set to a value other than 'none' and no transport-capacity exists, it shall be automatically created with the corresponding capacityMode.
            On network-connection deletion, if set to a value other than 'none', the supporting transport-capacity will be deleted.
            Depending on the requested service mode, the network-connection request with implicit transport-capacity creation may require additional parameters (e.g., endpoint capacity).
            If set to a value other than 'none' and the corresponding transport-capacity already exists, the transport-capacity capacityMode and endpoint capacity values must match the implicitTransportCapacity and endpoint capacity values in the network-connection request. 
            Otherwise, service creation is rejected.
             Possible Values: none, portMode, dedicatedDownlinkSymmetric, dedicatedDownlinkAsymmetric, sharedDownlink
        :labels: object - Assign key:value labels to objects
    """
    name = kwargs.get('name', None)
    serviceMode = kwargs.get('serviceMode', None)
    mc = kwargs.get('mc', None)
    outerVID = kwargs.get('outerVID', None)
    implicitTransportCapacity = kwargs.get('implicitTransportCapacity', None)
    labels = kwargs.get('labels', None)

    request = {
        "name": name,
        "serviceMode": serviceMode,
        "mc": mc,
        "outerVID": outerVID,
        "implicitTransportCapacity": implicitTransportCapacity,
        "labels": labels
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/network-connections/{ncId}")
    return response


def delete_network_connections(handle, ncId, **kwargs):
    """
    **Summary**
        ::
            Delete specific network connection
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/network-connections/{ncId}")
    return response


def get_network_connections_endpoints(handle, ncId, **kwargs):
    """
    **Summary**
        ::
            Retrieve network connection endpoints
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/network-connections/{ncId}/endpoints", q_value=q)
    return response


def create_network_connections_endpoints(handle, ncId, **kwargs):
    """
    **Summary**
        ::
            Create network connection endpoints
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
    
    
    **Optional Parameters**
        :capacity: integer - Client to network capacity of the attachment circuit.
            Possible values are defined in multiples of 25Gbps up to maximum module rate.
            
        :selector:
            hostPortSelectorByName :
                :hostName: string - User defined host name.
                
                :hostPortName: string - User defined host port name.
                
            hostPortSelectorByPortId :
                :chassisIdSubtype: string - Value of chassisIdSubtype (encoding of chassisId) within LLDP data.
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :chassisId: string - Value of chassisId within LLDP data
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :portIdSubtype: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
                :portId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
            hostPortSelectorBySysName :
                :sysName: string - Value of System Name within LLDP data
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :portIdSubtype: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
                :portId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
            hostPortSelectorByPortSourceMAC :
                :portSourceMAC: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the portSourceMAC.
                
            moduleIfSelectorByModuleId :
                :moduleId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules using moduleId.
                
                :moduleClientIfAid: string - TODO
                
            moduleIfSelectorByModuleName :
                :moduleName: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :moduleClientIfAid: string - TODO
                
            moduleIfSelectorByModuleMAC :
                :moduleMAC: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :moduleClientIfAid: string - TODO
                
            moduleIfSelectorByModuleSerialNumber :
                :moduleSerialNumber: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :moduleClientIfAid: string - TODO
                
    """
    capacity = kwargs.get('capacity', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    hostPortName = kwargs.get('hostPortName', None)
    chassisId = kwargs.get('chassisId', None)
    portSourceMAC = kwargs.get('portSourceMAC', None)
    moduleName = kwargs.get('moduleName', None)
    moduleClientIfAid = kwargs.get('moduleClientIfAid', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    moduleId = kwargs.get('moduleId', None)
    portId = kwargs.get('portId', None)
    portIdSubtype = kwargs.get('portIdSubtype', None)
    sysName = kwargs.get('sysName', None)
    hostName = kwargs.get('hostName', None)

    request = [
        {
            "selector": {
                "hostPortSelectorByName": {
                    "hostName": hostName,
                    "hostPortName": hostPortName
                },
                "hostPortSelectorByPortId": {
                    "chassisIdSubtype": chassisIdSubtype,
                    "chassisId": chassisId,
                    "portIdSubtype": portIdSubtype,
                    "portId": portId
                },
                "hostPortSelectorBySysName": {
                    "sysName": sysName,
                    "portIdSubtype": portIdSubtype,
                    "portId": portId
                },
                "hostPortSelectorByPortSourceMAC": {
                    "portSourceMAC": portSourceMAC
                },
                "moduleIfSelectorByModuleId": {
                    "moduleId": moduleId,
                    "moduleClientIfAid": moduleClientIfAid
                },
                "moduleIfSelectorByModuleName": {
                    "moduleName": moduleName,
                    "moduleClientIfAid": moduleClientIfAid
                },
                "moduleIfSelectorByModuleMAC": {
                    "moduleMAC": moduleMAC,
                    "moduleClientIfAid": moduleClientIfAid
                },
                "moduleIfSelectorByModuleSerialNumber": {
                    "moduleSerialNumber": moduleSerialNumber,
                    "moduleClientIfAid": moduleClientIfAid
                }
            },
            "capacity": capacity
        }
    ]

    request = xrutils.selector_parse(request, selector)
    response = xrutils.send_request(handle, "POST", f"/api/v1/network-connections/{ncId}/endpoints", request_body=request)
    return response


def get_network_connections_endpoints_by_epId(handle, ncId, epId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific endpoint data from a network connection
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
        :param epId: Endpoint identifier within the connection
        :type epId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/network-connections/{ncId}/endpoints/{epId}", q_value=q)
    return response


def update_network_connections_endpoints(handle, ncId, epId, **kwargs):
    """
    **Summary**
        ::
            Update specific network connection endpoint data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
        :param epId: Endpoint identifier within the connection
        :type epId: string
    
        :param capacity: Client to network capacity of the attachment circuit.
            Possible values are defined in multiples of 25Gbps up to maximum module rate.
            
        :type capacity: integer
    """
    capacity = kwargs.get('capacity', None)

    request = {
        "capacity": capacity
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/network-connections/{ncId}/endpoints/{epId}")
    return response


def delete_network_connections_endpoints(handle, ncId, epId, **kwargs):
    """
    **Summary**
        ::
            Delete specific network connection endpoint
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param ncId: Connection identifier within the connection list
        :type ncId: string
        :param epId: Endpoint identifier within the connection
        :type epId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/network-connections/{ncId}/endpoints/{epId}")
    return response


def get_lcs(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all local connections with associated network connections information
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/lcs", q_value=q)
    return response


def get_lcs_by_lcId(handle, lcId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific local connection data with associated network connections
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param lcId: Local connection identifier within the connection scope
        :type lcId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/lcs/{lcId}", q_value=q)
    return response


def get_acs(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all attachment circuits with associated network connections information
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/acs", q_value=q)
    return response


def get_acs_by_acId(handle, acId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific attachment circuit data with associated network connections
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param acId: Attachment circuit identifier within the connection scope
        :type acId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/acs/{acId}", q_value=q)
    return response


def get_ndus(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDUs
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus", q_value=q)
    return response


def get_ndus_by_nduId(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}", q_value=q)
    return response


def update_ndus(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            update NDU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    
    **Optional Parameters**
        :name: string - Property to change the NDU name. 
            This is also reflected in the same property in oic.wk.d
            
        :description: string - NE location, defined by operator.
        :clli: string - Common Location Language Identifier
        :latitude: integer - Latitude location info.  Range: -90.0 to +90.0
            
        :longitude: integer - Longitude location info.  Range: -180.0 to +180.0
            
        :altitude: integer - 
        :contact: string - Contact info of administrator of NDU
        :managedBy: string - Defines the ownership of the object. Possible Values: local, CM
        :labels: object - Assign key:value labels to objects
        :polPowerCtrlMode: string - Pluggable optical interface power control mode setting configured by user. Should be set to 'manual' if NDU manually shall set booster gain (e.g. when amplification needed after mux but with no XR power control).   Value 'auto' automatically detects presence of QSFP-EDFA or QSFP-VOA in port 4.
             Possible Values: manual
    """
    name = kwargs.get('name', None)
    description = kwargs.get('description', None)
    clli = kwargs.get('clli', None)
    latitude = kwargs.get('latitude', None)
    longitude = kwargs.get('longitude', None)
    altitude = kwargs.get('altitude', None)
    contact = kwargs.get('contact', None)
    managedBy = kwargs.get('managedBy', None)
    labels = kwargs.get('labels', None)
    polPowerCtrlMode = kwargs.get('polPowerCtrlMode', None)

    request = {
        "name": name,
        "location": {
            "description": description,
            "clli": clli,
            "latitude": latitude,
            "longitude": longitude,
            "altitude": altitude
        },
        "contact": contact,
        "managedBy": managedBy,
        "labels": labels,
        "polPowerCtrlMode": polPowerCtrlMode
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}")
    return response


def delete_ndus(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            delete specific NDU
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/ndus/{nduId}")
    return response


def get_ndus_fanUnit(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU fan unit data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/fanUnit", q_value=q)
    return response


def get_ndus_pem(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU PEM unit data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/pem", q_value=q)
    return response


def get_ndus_leds(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU leds data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/leds", q_value=q)
    return response


def perform_ndus_coldStart(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            NDU Cold Start operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/coldStart", request_body=request)
    return response


def perform_ndus_warmStart(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            NDU Warm Start operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/warmStart", request_body=request)
    return response


def perform_ndus_factoryReset(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            NDU Factory reset operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/factoryReset", request_body=request)
    return response


def perform_ndus_retry(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/retry", request_body=request)
    return response


def perform_ndus_adopt(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/adopt", request_body=request)
    return response


def get_ndus_ports(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU ports
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports", q_value=q)
    return response


def get_ndus_ports_by_nduPortColId(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU port data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}", q_value=q)
    return response


def update_ndus_ports(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU port data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :connectedTo: string - User configurable neighbor entity information
    """
    name = kwargs.get('name', None)
    connectedTo = kwargs.get('connectedTo', None)

    request = {
        "name": name,
        "connectedTo": connectedTo
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}")
    return response


def perform_ndus_ports_retry(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU port configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/retry", request_body=request)
    return response


def perform_ndus_ports_adopt(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU port configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/adopt", request_body=request)
    return response


def get_ndus_ports_tom(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU TOMs
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tom", q_value=q)
    return response


def create_ndus_ports_tom(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Create NDU TOM
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :requiredType: string - User intent of the TOM type that is expected to be installed at this port. Possible Values: QSFP28
        :requiredSubType: string - User intent of the TOM subtype that is expected to be installed at this port. Possible Values: TOM-100G-Q, TOM-100G-Q-SR4, TOM-100G-Q-LR4, ZXS-Q8PSM4ZZ-00, ZXS-Q8L4ZZZZ-ET, TOM-100GMR-Q-SR4, TOM-100GMR-Q-LR4, TOM-100G-Q-CWDM4, TOM-100G-Q-ER4L
        :phyMode: string - List of supported physical modes for this TOM (based on TOM type) Supported physical modes: * '100GE': 
                - TOM-100G-Q, 
                - TOM-100G-Q-SR4, 
                - TOM-100G-Q-LR4, 
                - ZXS-Q8PSM4ZZ-00, 
                - ZXS-Q8L4ZZZZ-ET, 
                - TOM-100GMR-Q-SR4, 
                - TOM-100GMR-Q-LR4, 
                - TOM-100G-Q-CWDM4, 
                - TOM-100G-Q-ER4L
            * 4x25GE: 
                - ZXS-Q8PSM4ZZ-00
            * OTU4:
                - TOM-100GMR-Q-SR4
                - TOM-100GMR-Q-LR4
             Possible Values: 100GE, 4x25GE, OTU4
    """
    name = kwargs.get('name', None)
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    phyMode = kwargs.get('phyMode', None)

    request = {
        "name": name,
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "phyMode": phyMode
    }

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tom", request_body=request)
    return response


def get_ndus_ports_tom_by_nduTomColId(handle, nduId, nduPortColId, nduTomColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU port TOM data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTomColId: Tom identifier within NDU port.
        :type nduTomColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tom/{nduTomColId}", q_value=q)
    return response


def update_ndus_ports_tom(handle, nduId, nduPortColId, nduTomColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU port TOM data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTomColId: Tom identifier within NDU port.
        :type nduTomColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :requiredType: string - User intent of the TOM type that is expected to be installed at this port. Possible Values: QSFP28
        :requiredSubType: string - User intent of the TOM subtype that is expected to be installed at this port. Possible Values: TOM-100G-Q, TOM-100G-Q-SR4, TOM-100G-Q-LR4, ZXS-Q8PSM4ZZ-00, ZXS-Q8L4ZZZZ-ET, TOM-100GMR-Q-SR4, TOM-100GMR-Q-LR4, TOM-100G-Q-CWDM4, TOM-100G-Q-ER4L
        :phyMode: string - List of supported physical modes for this TOM (based on TOM type) Supported physical modes: * '100GE': 
                - TOM-100G-Q, 
                - TOM-100G-Q-SR4, 
                - TOM-100G-Q-LR4, 
                - ZXS-Q8PSM4ZZ-00, 
                - ZXS-Q8L4ZZZZ-ET, 
                - TOM-100GMR-Q-SR4, 
                - TOM-100GMR-Q-LR4, 
                - TOM-100G-Q-CWDM4, 
                - TOM-100G-Q-ER4L
            * 4x25GE: 
                - ZXS-Q8PSM4ZZ-00
            * OTU4:
                - TOM-100GMR-Q-SR4
                - TOM-100GMR-Q-LR4
             Possible Values: 100GE, 4x25GE, OTU4
    """
    name = kwargs.get('name', None)
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    phyMode = kwargs.get('phyMode', None)

    request = {
        "name": name,
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "phyMode": phyMode
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tom/{nduTomColId}")
    return response


def delete_ndus_ports_tom(handle, nduId, nduPortColId, nduTomColId, **kwargs):
    """
    **Summary**
        ::
            Delete specific NDU port TOM
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTomColId: Tom identifier within NDU port.
        :type nduTomColId: integer
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tom/{nduTomColId}")
    return response


def perform_ndus_ports_tom_retry(handle, nduId, nduPortColId, nduTomColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for TOM configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTomColId: Tom identifier within NDU port.
        :type nduTomColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tom/{nduTomColId}/retry", request_body=request)
    return response


def perform_ndus_ports_tom_adopt(handle, nduId, nduPortColId, nduTomColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for TOM configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTomColId: Tom identifier within NDU port.
        :type nduTomColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tom/{nduTomColId}/adopt", request_body=request)
    return response


def get_ndus_ports_xr(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU XR pluggable interfaces
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr", q_value=q)
    return response


def create_ndus_ports_xr(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Create NDU XR
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    
    **Optional Parameters**
        :requiredType: string - User intent of the pluggable interface type that is expected to be installed at this port. Possible Values: CFP2-DCO
        :requiredSubType: string - User intent of the pluggable interface subtype that is expected to be installed at this port.
             Possible Values: CFP2-DCO-400G, CFP2-DCO-200G, CFP2-DCO-100G
        :name: string - User defined label
    """
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    name = kwargs.get('name', None)

    request = {
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "name": name
    }

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr", request_body=request)
    return response


def get_ndus_ports_xr_by_nduXrColId(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU port XR pluggable data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}", q_value=q)
    return response


def update_ndus_ports_xr(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU port XR pluggable data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    
    **Optional Parameters**
        :requiredType: string - User intent of the pluggable interface type that is expected to be installed at this port. Possible Values: CFP2-DCO
        :requiredSubType: string - User intent of the pluggable interface subtype that is expected to be installed at this port.
             Possible Values: CFP2-DCO-400G, CFP2-DCO-200G, CFP2-DCO-100G
        :name: string - User defined label
    """
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    name = kwargs.get('name', None)

    request = {
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "name": name
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}")
    return response


def delete_ndus_ports_xr(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            Delete specific NDU port Xr pluggable interface
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}")
    return response


def perform_ndus_ports_xr_coldStart(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            NDU XR Cold Start operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}/coldStart", request_body=request)
    return response


def perform_ndus_ports_xr_warmStart(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            NDU XR Warm Start operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}/warmStart", request_body=request)
    return response


def perform_ndus_ports_xr_factoryReset(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            NDU XR Factory reset operation
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}/factoryReset", request_body=request)
    return response


def perform_ndus_ports_xr_retry(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU XR configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}/retry", request_body=request)
    return response


def perform_ndus_ports_xr_adopt(handle, nduId, nduPortColId, nduXrColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU XR configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduXrColId: XR pluggable identifier within NDU port.
        :type nduXrColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/xr/{nduXrColId}/adopt", request_body=request)
    return response


def get_ndus_ports_edfa(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU EDFAa
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/edfa", q_value=q)
    return response


def create_ndus_ports_edfa(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Create NDU EDFA
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    
    **Optional Parameters**
        :requiredType: string - User intent of the pluggable interface type that is expected to be installed at this port. Possible Values: QSFP28
        :requiredSubType: string - User intent of the pluggable interface subtype that is expected to be installed at this port. Possible Values: QSFP28EDFA
        :name: string - User defined label
        :amplifierEnable: boolean - The enable switch for the amplifier.
        :gainTarget: integer - Target gain to be achieved by the amplifier in dB*10. Possible values: 0 to 40.0 dB. Default: 0
            
    """
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    name = kwargs.get('name', None)
    amplifierEnable = kwargs.get('amplifierEnable', None)
    gainTarget = kwargs.get('gainTarget', None)

    request = {
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "name": name,
        "amplifierEnable": amplifierEnable,
        "gainTarget": gainTarget
    }

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/edfa", request_body=request)
    return response


def get_ndus_ports_edfa_by_nduEdfaColId(handle, nduId, nduPortColId, nduEdfaColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU port EDFA data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduEdfaColId: Edfa identifier within NDU port.
        :type nduEdfaColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/edfa/{nduEdfaColId}", q_value=q)
    return response


def update_ndus_ports_edfa(handle, nduId, nduPortColId, nduEdfaColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU port EDFA data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduEdfaColId: Edfa identifier within NDU port.
        :type nduEdfaColId: integer
    
    
    **Optional Parameters**
        :requiredType: string - User intent of the pluggable interface type that is expected to be installed at this port. Possible Values: QSFP28
        :requiredSubType: string - User intent of the pluggable interface subtype that is expected to be installed at this port. Possible Values: QSFP28EDFA
        :name: string - User defined label
        :amplifierEnable: boolean - The enable switch for the amplifier.
        :gainTarget: integer - Target gain to be achieved by the amplifier in dB*10. Possible values: 0 to 40.0 dB. Default: 0
            
    """
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    name = kwargs.get('name', None)
    amplifierEnable = kwargs.get('amplifierEnable', None)
    gainTarget = kwargs.get('gainTarget', None)

    request = {
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "name": name,
        "amplifierEnable": amplifierEnable,
        "gainTarget": gainTarget
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/edfa/{nduEdfaColId}")
    return response


def delete_ndus_ports_edfa(handle, nduId, nduPortColId, nduEdfaColId, **kwargs):
    """
    **Summary**
        ::
            Delete specific NDU port EDFA
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduEdfaColId: Edfa identifier within NDU port.
        :type nduEdfaColId: integer
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/edfa/{nduEdfaColId}")
    return response


def perform_ndus_ports_edfa_retry(handle, nduId, nduPortColId, nduEdfaColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU EDFA configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduEdfaColId: Edfa identifier within NDU port.
        :type nduEdfaColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/edfa/{nduEdfaColId}/retry", request_body=request)
    return response


def perform_ndus_ports_edfa_adopt(handle, nduId, nduPortColId, nduEdfaColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU EDFA configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduEdfaColId: Edfa identifier within NDU port.
        :type nduEdfaColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/edfa/{nduEdfaColId}/adopt", request_body=request)
    return response


def get_ndus_ports_voa(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU VOAs
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/voa", q_value=q)
    return response


def create_ndus_ports_voa(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Create NDU VOA
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    
    **Optional Parameters**
        :requiredType: string - User intent of the pluggable interface type that is expected to be installed at this port. Possible Values: QSFP28
        :requiredSubType: string - User intent of the pluggable interface subtype that is expected to be installed at this port. Possible Values: QSFP28VOA
        :name: string - User defined label
        :voaShutterTx: boolean - Shutter mode for the VOA.
        :voaAttenuationTx: integer - Attenuation setting on VOA in dB*10. Possible values: 0 to 40 dB. Default: 0
            
    """
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    name = kwargs.get('name', None)
    voaShutterTx = kwargs.get('voaShutterTx', None)
    voaAttenuationTx = kwargs.get('voaAttenuationTx', None)

    request = {
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "name": name,
        "voaShutterTx": voaShutterTx,
        "voaAttenuationTx": voaAttenuationTx
    }

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/voa", request_body=request)
    return response


def get_ndus_ports_voa_by_nduVoaColId(handle, nduId, nduPortColId, nduVoaColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU port VOA data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduVoaColId: VOA identifier within NDU port.
        :type nduVoaColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/voa/{nduVoaColId}", q_value=q)
    return response


def update_ndus_ports_voa(handle, nduId, nduPortColId, nduVoaColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU port VOA data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduVoaColId: VOA identifier within NDU port.
        :type nduVoaColId: integer
    
    
    **Optional Parameters**
        :requiredType: string - User intent of the pluggable interface type that is expected to be installed at this port. Possible Values: QSFP28
        :requiredSubType: string - User intent of the pluggable interface subtype that is expected to be installed at this port. Possible Values: QSFP28VOA
        :name: string - User defined label
        :voaShutterTx: boolean - Shutter mode for the VOA.
        :voaAttenuationTx: integer - Attenuation setting on VOA in dB*10. Possible values: 0 to 40 dB. Default: 0
            
    """
    requiredType = kwargs.get('requiredType', None)
    requiredSubType = kwargs.get('requiredSubType', None)
    name = kwargs.get('name', None)
    voaShutterTx = kwargs.get('voaShutterTx', None)
    voaAttenuationTx = kwargs.get('voaAttenuationTx', None)

    request = {
        "requiredType": requiredType,
        "requiredSubType": requiredSubType,
        "name": name,
        "voaShutterTx": voaShutterTx,
        "voaAttenuationTx": voaAttenuationTx
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/voa/{nduVoaColId}")
    return response


def delete_ndus_ports_voa(handle, nduId, nduPortColId, nduVoaColId, **kwargs):
    """
    **Summary**
        ::
            Delete specific NDU port VOA
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduVoaColId: VOA identifier within NDU port.
        :type nduVoaColId: integer
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/voa/{nduVoaColId}")
    return response


def perform_ndus_ports_voa_retry(handle, nduId, nduPortColId, nduVoaColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU VOA configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduVoaColId: VOA identifier within NDU port.
        :type nduVoaColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/voa/{nduVoaColId}/retry", request_body=request)
    return response


def perform_ndus_ports_voa_adopt(handle, nduId, nduPortColId, nduVoaColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU VOA configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduVoaColId: VOA identifier within NDU port.
        :type nduVoaColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/voa/{nduVoaColId}/adopt", request_body=request)
    return response


def get_ndus_ports_linePtps(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of NDU line physical termination points
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps", q_value=q)
    return response


def get_ndus_ports_linePtps_by_nduLinePtpColId(handle, nduId, nduPortColId, nduLinePtpColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU line physical termination point data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}", q_value=q)
    return response


def update_ndus_ports_linePtps(handle, nduId, nduPortColId, nduLinePtpColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU XR port line physical termination point data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :txLaserEnable: boolean - Enable switch for the line pluggable laser.
    """
    name = kwargs.get('name', None)
    txLaserEnable = kwargs.get('txLaserEnable', None)

    request = {
        "name": name,
        "txLaserEnable": txLaserEnable
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}")
    return response


def perform_ndus_ports_linePtps_retry(handle, nduId, nduPortColId, nduLinePtpColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU port linePtp configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}/retry", request_body=request)
    return response


def perform_ndus_ports_linePtps_adopt(handle, nduId, nduPortColId, nduLinePtpColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU port linePtp configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}/adopt", request_body=request)
    return response


def get_ndus_ports_polPtps(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of NDU pluggable optical layer physical termination points
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/polPtps", q_value=q)
    return response


def get_ndus_ports_polPtps_by_nduPolPtpColId(handle, nduId, nduPortColId, nduPolPtpColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU pluggable optical layer physical termination point data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduPolPtpColId: Pluggable optical layer PTP identifier within NDU.
        :type nduPolPtpColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/polPtps/{nduPolPtpColId}", q_value=q)
    return response


def update_ndus_ports_polPtps(handle, nduId, nduPortColId, nduPolPtpColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU pluggable optical layer physical termination point data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduPolPtpColId: Pluggable optical layer PTP identifier within NDU.
        :type nduPolPtpColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
    """
    name = kwargs.get('name', None)

    request = {
        "name": name
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/polPtps/{nduPolPtpColId}")
    return response


def perform_ndus_ports_polPtps_retry(handle, nduId, nduPortColId, nduPolPtpColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU port polPtp configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduPolPtpColId: Pluggable optical layer PTP identifier within NDU.
        :type nduPolPtpColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/polPtps/{nduPolPtpColId}/retry", request_body=request)
    return response


def perform_ndus_ports_polPtps_adopt(handle, nduId, nduPortColId, nduPolPtpColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU port polPtp configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduPolPtpColId: Pluggable optical layer PTP identifier within NDU.
        :type nduPolPtpColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/polPtps/{nduPolPtpColId}/adopt", request_body=request)
    return response


def get_ndus_ports_tribPtps(handle, nduId, nduPortColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of NDU port tributary physical termination points
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tribPtps", q_value=q)
    return response


def get_ndus_ports_tribPtps_by_nduTribPtpColId(handle, nduId, nduPortColId, nduTribPtpColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU port tributary physical termination point data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTribPtpColId: Tributary PTP identifier within NDU.
        :type nduTribPtpColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tribPtps/{nduTribPtpColId}", q_value=q)
    return response


def update_ndus_ports_tribPtps(handle, nduId, nduPortColId, nduTribPtpColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU tributary port physical termination points data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTribPtpColId: Tributary PTP identifier within NDU.
        :type nduTribPtpColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :txLaserEnable: boolean - Enable switch for the line pluggable laser.
    """
    name = kwargs.get('name', None)
    txLaserEnable = kwargs.get('txLaserEnable', None)

    request = {
        "name": name,
        "txLaserEnable": txLaserEnable
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tribPtps/{nduTribPtpColId}")
    return response


def perform_ndus_ports_tribPtps_retry(handle, nduId, nduPortColId, nduTribPtpColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU port tribPtp configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTribPtpColId: Tributary PTP identifier within NDU.
        :type nduTribPtpColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tribPtps/{nduTribPtpColId}/retry", request_body=request)
    return response


def perform_ndus_ports_tribPtps_adopt(handle, nduId, nduPortColId, nduTribPtpColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU port tribPtp configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduTribPtpColId: Tributary PTP identifier within NDU.
        :type nduTribPtpColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/tribPtps/{nduTribPtpColId}/adopt", request_body=request)
    return response


def get_ndus_ports_linePtps_carrier(handle, nduId, nduPortColId, nduLinePtpColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU line port carriers
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}/carrier", q_value=q)
    return response


def get_ndus_ports_linePtps_carrier_by_nduCarrierColId(handle, nduId, nduPortColId, nduLinePtpColId, nduCarrierColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU line port carrier data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
        :param nduCarrierColId: Carrier identifier within NDU line port.
        :type nduCarrierColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}/carrier/{nduCarrierColId}", q_value=q)
    return response


def update_ndus_ports_linePtps_carrier(handle, nduId, nduPortColId, nduLinePtpColId, nduCarrierColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU XR port carrier data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
        :param nduCarrierColId: Carrier identifier within NDU line port.
        :type nduCarrierColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :frequency: integer - Carrier Center Frequency configured by the Host via MSA interface. Optionally, in a Leaf module it might include an offset in 6.25GHz granularity if a Host has configured the service using frequency overload feature. Possible values: - Minimum: 191275000  - Maximum: 196150000 Or - Value '191100000': used for auto-lambda function
            
        :modulation: string - Carrier Modulation configured by the Host via MSA interface. Possible Values: QPSK, 8QAM, 16QAM
        :txCLPtarget: integer - Tx Carrier Launch Target Power configured by the host via MSA interface in hundreds of dBm. Possible values: - Minimum: -3600 dBm - Maximum: 300 dBm Or - Value '-99.00' is used for "Undefined".
            
        :termLB: string - Enable/Disable terminal loopback. Loopback type: - disabled - loopback            - Signal is looped back and LF maintenance signal is sent downstream.
             Possible Values: disabled, loopbackAndContinue
        :termLBDuration: integer - Duration of the terminal loopback configuration in seconds. After the specified time, module automatically disables the terminal loopback. 0 value is used for indefinitely.
            
        :facPRBSGen: boolean - Enable/Disable facility PRBS test pattern generation
        :facPRBSMon: boolean - Enable/Disable facility PRBS test pattern monitoring
    """
    name = kwargs.get('name', None)
    frequency = kwargs.get('frequency', None)
    modulation = kwargs.get('modulation', None)
    txCLPtarget = kwargs.get('txCLPtarget', None)
    termLB = kwargs.get('termLB', None)
    termLBDuration = kwargs.get('termLBDuration', None)
    facPRBSGen = kwargs.get('facPRBSGen', None)
    facPRBSMon = kwargs.get('facPRBSMon', None)

    request = {
        "name": name,
        "frequency": frequency,
        "modulation": modulation,
        "txCLPtarget": txCLPtarget,
        "diagnostics": {
            "termLB": termLB,
            "termLBDuration": termLBDuration,
            "facPRBSGen": facPRBSGen,
            "facPRBSMon": facPRBSMon
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}/carrier/{nduCarrierColId}")
    return response


def perform_ndus_ports_linePtps_carrier_retry(handle, nduId, nduPortColId, nduLinePtpColId, nduCarrierColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU carrier configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
        :param nduCarrierColId: Carrier identifier within NDU line port.
        :type nduCarrierColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}/carrier/{nduCarrierColId}/retry", request_body=request)
    return response


def perform_ndus_ports_linePtps_carrier_adopt(handle, nduId, nduPortColId, nduLinePtpColId, nduCarrierColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU carrier configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduPortColId: NDU port identifier within NDU.
        :type nduPortColId: integer
        :param nduLinePtpColId: Line PTP identifier within NDU.
        :type nduLinePtpColId: integer
        :param nduCarrierColId: Carrier identifier within NDU line port.
        :type nduCarrierColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ports/{nduPortColId}/linePtps/{nduLinePtpColId}/carrier/{nduCarrierColId}/adopt", request_body=request)
    return response


def get_ndus_otus(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU OTU clients
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/otus", q_value=q)
    return response


def get_ndus_otus_by_nduOtuColId(handle, nduId, nduOtuColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU OTU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduOtuColId: OTU signal identifier within NDU.
        :type nduOtuColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/otus/{nduOtuColId}", q_value=q)
    return response


def update_ndus_otus(handle, nduId, nduOtuColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU OTU data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduOtuColId: OTU signal identifier within NDU.
        :type nduOtuColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :fecMode: string - Forward error correction mode of operation. Only applicable for client OTU signals (always enabled for line side OTU signals).
             Possible Values: enabled, disabled
        :termLB: string - Enable/Disable terminal loopback. Only applicable for client OTU signals. Loopback type:
             * 'disabled'
             * 'loopback':             Signal is looped back and LF maintenance signal is sent downstream.
             * 'loopbackAndContinue':  Signal is looped back and is also forwarded downstream.
                                       Only applicable for client OTU signals.
             Possible Values: disabled, loopback, loopbackAndContinue
        :termLBDuration: integer - Duration of the terminal loopback configuration in seconds. Only applicable for client OTU signals. After the specified time, module automatically disables the terminal loopback. 0 value is used for indefinitely.
            
        :facLB: string - Post-FEC facility loopback mode for the OTU signal. Only applicable for client OTU signals. Loopback type:
              * 'disabled'
              * 'loopback':             Signal is looped back and LF maintenance signal is sent downstream.
              * 'loopbackAndContinue':  Signal is looped back and is also forwarded downstream.
             Possible Values: disabled, loopback, loopbackAndContinue
        :facLBDuration: integer - Duration of the facility loopback configuration in seconds. Only applicable for client OTU signals. After the specified time, module automatically disables the facility loopback. 0 value is used for indefinitely.
            
    """
    name = kwargs.get('name', None)
    fecMode = kwargs.get('fecMode', None)
    termLB = kwargs.get('termLB', None)
    termLBDuration = kwargs.get('termLBDuration', None)
    facLB = kwargs.get('facLB', None)
    facLBDuration = kwargs.get('facLBDuration', None)

    request = {
        "name": name,
        "fecMode": fecMode,
        "diagnostics": {
            "termLB": termLB,
            "termLBDuration": termLBDuration,
            "facLB": facLB,
            "facLBDuration": facLBDuration
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/otus/{nduOtuColId}")
    return response


def perform_ndus_otus_retry(handle, nduId, nduOtuColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU OTU configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduOtuColId: OTU signal identifier within NDU.
        :type nduOtuColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/otus/{nduOtuColId}/retry", request_body=request)
    return response


def perform_ndus_otus_adopt(handle, nduId, nduOtuColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU OTU configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduOtuColId: OTU signal identifier within NDU.
        :type nduOtuColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/otus/{nduOtuColId}/adopt", request_body=request)
    return response


def get_ndus_ethernets(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU ethernet clients
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ethernets", q_value=q)
    return response


def get_ndus_ethernets_by_nduEthernetColId(handle, nduId, nduEthernetColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU ethernet client data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduEthernetColId: Ethernet client signal identifier within NDU.
        :type nduEthernetColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/ethernets/{nduEthernetColId}", q_value=q)
    return response


def update_ndus_ethernets(handle, nduId, nduEthernetColId, **kwargs):
    """
    **Summary**
        ::
            Update NDU Ethernet client data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduEthernetColId: Ethernet client signal identifier within NDU.
        :type nduEthernetColId: integer
    
    
    **Optional Parameters**
        :name: string - User defined label
        :fecMode: string - Forward error correction mode of operation Possible Values: enabled, disabled
        :termLB: string - Post-FEC terminal loopback mode for the ethernet client. Loopback type:
              * disabled
              * loopback            - Signal is looped back and LF maintenance signal is sent downstream.
              * loopbackAndContinue - Signal is looped back and is also forwarded downstream.
             Possible Values: disabled, loopback, loopbackAndContinue
        :termLBDuration: integer - Duration of the terminal loopback configuration in seconds. After the specified time, module automatically disables the terminal loopback. 0 value is used for indefinitely.
            
        :facLB: string - Post-FEC facility loopback mode for the ethernet client. Loopback type:
              * disabled
              * loopback            - Signal is looped back and LF maintenance signal is sent downstream.
              * loopbackAndContinue - Signal is looped back and is also forwarded downstream.
             Possible Values: disabled, loopback, loopbackAndContinue
        :facLBDuration: integer - Duration of the facility loopback configuration in seconds. After the specified time, module automatically disables the facility loopback. 0 value is used for indefinitely.
            
        :facTestSignalGen: string - Allows selection of test signal type for generation towards host.
            Possible values:
              * 'disabled':       Used when no test signal insertion is required.
              * 'scrambledIdle':  Inserts Idle towards host.
              * 'prbs31':         Insert per-lane PRBS31 towards host.
             Possible Values: disabled, scrambledIdle, prbs31
        :facTestSignalMon: string - Allows selection of test signal type for monitoring in host ingress direction.
            Possible values:
              * 'disabled':       Used when no test signal monitoring is required.
              * 'scrambledIdle':  Idle signal monitoring from host.
              * 'prbs31':         Per-lane signal monitoring from host.
             Possible Values: disabled, scrambledIdle, prbs31
        :termTestSignalGen: string - Allows selection of test signal type for generation towards network direction.
            Possible values:
            - 'disabled':       Used when no test signal insertion is required.
            - 'scrambledIdle':  Insert PCS Idle towards towards network direction.
             Possible Values: disabled, scrambledIdle
    """
    name = kwargs.get('name', None)
    fecMode = kwargs.get('fecMode', None)
    termLB = kwargs.get('termLB', None)
    termLBDuration = kwargs.get('termLBDuration', None)
    facLB = kwargs.get('facLB', None)
    facLBDuration = kwargs.get('facLBDuration', None)
    facTestSignalGen = kwargs.get('facTestSignalGen', None)
    facTestSignalMon = kwargs.get('facTestSignalMon', None)
    termTestSignalGen = kwargs.get('termTestSignalGen', None)

    request = {
        "name": name,
        "fecMode": fecMode,
        "diagnostics": {
            "termLB": termLB,
            "termLBDuration": termLBDuration,
            "facLB": facLB,
            "facLBDuration": facLBDuration,
            "facTestSignalGen": facTestSignalGen,
            "facTestSignalMon": facTestSignalMon,
            "termTestSignalGen": termTestSignalGen
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/ndus/{nduId}/ethernets/{nduEthernetColId}")
    return response


def perform_ndus_ethernets_retry(handle, nduId, nduEthernetColId, **kwargs):
    """
    **Summary**
        ::
            Retry operation for NDU ethernet configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduEthernetColId: Ethernet client signal identifier within NDU.
        :type nduEthernetColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ethernets/{nduEthernetColId}/retry", request_body=request)
    return response


def perform_ndus_ethernets_adopt(handle, nduId, nduEthernetColId, **kwargs):
    """
    **Summary**
        ::
            Adopt operation for NDU ethernet configurations
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduEthernetColId: Ethernet client signal identifier within NDU.
        :type nduEthernetColId: integer
    
    """
    request = {}

    response = xrutils.send_request(handle, "POST", f"/api/v1/ndus/{nduId}/ethernets/{nduEthernetColId}/adopt", request_body=request)
    return response


def get_ndus_lcs(handle, nduId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all NDU lcs
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/lcs", q_value=q)
    return response


def get_ndus_lcs_by_nduLcColId(handle, nduId, nduLcColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific NDU lc data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param nduId: NDU identifier.
        :type nduId: string
        :param nduLcColId: Local connection identifier within NDU.
        :type nduLcColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/ndus/{nduId}/lcs/{nduLcColId}", q_value=q)
    return response


def get_xr_networks(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all xr-network objects
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/xr-networks", q_value=q)
    return response


def build_hubModule(handle, **kwargs):
    """
    **Summary**
        ::
            Helper method for create_xr_networks

        :param handle: xrctrl connection handle
        :type handle: string
        :param trafficMode: Possible Values:
            - L1Mode: Allows transparent transport of client traffic between XR hub and leaf module client ports
            - VTIMode: Allows transport of VLAN flows between an XR hub module client port to 1 or more XR leaf module client ports
            
        :type trafficMode: string
    
    **Optional Parameters**
        :plannedCapacity: string - Module planned capacity.
            Default and possible values are dependent of module type, capabilities, fiber connection mode and carrier modulation.
             Possible Values: 400G, 200G, 100G, 50G, 25G
        :fiberConnectionMode: string - Possible Values:
            - single: only one fiber is connected for by-directional traffic
            - dual: separate fibers for transmit and receive
            
        :requestedNominalPsdOffset: string - Requested Nominal PSD Offset
            This parameter is used to calculate the module's maxTxDSC
             Possible Values: 0dB, +3dB, +6dB
        :fecIterations: string - FEC iterations.
            Possible values:
            - undefined
            - standard      Standard is 2 FEC iterations.
            - turbo         Turbo is 3 FEC iterations.
             Possible Values: undefined, standard, turbo
        :txCLPtarget: integer - Tx Carrier Launch Target Power in hundreds of dBm.
            Possible values:
            - Minimum: -3600
            - Maximum: 300
              Or
            - Value '-99.00': used for "Undefined".
            
    **Selector**
        :param selector: - 
            moduleSelectorByModuleId :
                moduleId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules using moduleId.
            moduleSelectorByModuleName :
                moduleName - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
            moduleSelectorByModuleMAC :
                moduleMAC - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
            moduleSelectorByModuleSerialNumber :
                moduleSerialNumber - string - Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
            hostPortSelectorByName :
                hostName - string - User defined host name.
                hostPortName - string - User defined host port name.
            hostPortSelectorByPortId :
                chassisIdSubtype - string - Value of chassisIdSubtype (encoding of 
                    chassisId) within LLDP data. Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
                chassisId - string - Value of chassisId within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorBySysName :
                sysName - string - Value of System Name within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorByPortSourceMAC :
                portSourceMAC - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    portSourceMAC.
    """
    plannedCapacity = kwargs.get('plannedCapacity', None)
    fiberConnectionMode = kwargs.get('fiberConnectionMode', None)
    requestedNominalPsdOffset = kwargs.get('requestedNominalPsdOffset', None)
    trafficMode = kwargs.get('trafficMode', None)
    fecIterations = kwargs.get('fecIterations', None)
    txCLPtarget = kwargs.get('txCLPtarget', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    hostPortName = kwargs.get('hostPortName', None)
    chassisId = kwargs.get('chassisId', None)
    moduleName = kwargs.get('moduleName', None)
    portSourceMAC = kwargs.get('portSourceMAC', None)
    moduleId = kwargs.get('moduleId', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    portId = kwargs.get('portId', None)
    portIdSubtype = kwargs.get('portIdSubtype', None)
    sysName = kwargs.get('sysName', None)
    hostName = kwargs.get('hostName', None)

    data = {
        "selector": {
            "moduleSelectorByModuleId": {
                "moduleId": moduleId
            },
            "moduleSelectorByModuleName": {
                "moduleName": moduleName
            },
            "moduleSelectorByModuleMAC": {
                "moduleMAC": moduleMAC
            },
            "moduleSelectorByModuleSerialNumber": {
                "moduleSerialNumber": moduleSerialNumber
            },
            "hostPortSelectorByName": {
                "hostName": hostName,
                "hostPortName": hostPortName
            },
            "hostPortSelectorByPortId": {
                "chassisIdSubtype": chassisIdSubtype,
                "chassisId": chassisId,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorBySysName": {
                "sysName": sysName,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorByPortSourceMAC": {
                "portSourceMAC": portSourceMAC
            }
        },
        "module": {
            "plannedCapacity": plannedCapacity,
            "fiberConnectionMode": fiberConnectionMode,
            "requestedNominalPsdOffset": requestedNominalPsdOffset,
            "trafficMode": trafficMode,
            "fecIterations": fecIterations,
            "txCLPtarget": txCLPtarget
        }
    }

    data = xrutils.selector_parse(data, selector)
    return data


def build_leafModule(handle, **kwargs):
    """
    **Summary**
        ::
            Helper method for create_xr_networks

        :param handle: xrctrl connection handle
        :type handle: string
        :param trafficMode: Possible Values:
            - L1Mode: Allows transparent transport of client traffic between XR hub and leaf module client ports
            - VTIMode: Allows transport of VLAN flows between an XR hub module client port to 1 or more XR leaf module client ports
            
        :type trafficMode: string
    
    **Optional Parameters**
        :plannedCapacity: string - Module planned capacity.
            Default and possible values are dependent of module type, capabilities, fiber connection mode and carrier modulation.
             Possible Values: 400G, 200G, 100G, 50G, 25G
        :fiberConnectionMode: string - Possible Values:
            - single: only one fiber is connected for by-directional traffic
            - dual: separate fibers for transmit and receive
            
        :requestedNominalPsdOffset: string - Requested Nominal PSD Offset
            This parameter is used to calculate the module's maxTxDSC
             Possible Values: 0dB, +3dB, +6dB
        :fecIterations: string - FEC iterations.
            Possible values:
            - undefined
            - standard      Standard is 2 FEC iterations.
            - turbo         Turbo is 3 FEC iterations.
             Possible Values: undefined, standard, turbo
        :txCLPtarget: integer - Tx Carrier Launch Target Power in hundreds of dBm.
            Possible values:
            - Minimum: -3600
            - Maximum: 300
              Or
            - Value '-99.00': used for "Undefined".
            
    **Selector**
        :param selector: - 
            moduleSelectorByModuleId :
                moduleId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules using moduleId.
            moduleSelectorByModuleName :
                moduleName - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
            moduleSelectorByModuleMAC :
                moduleMAC - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
            moduleSelectorByModuleSerialNumber :
                moduleSerialNumber - string - Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
            hostPortSelectorByName :
                hostName - string - User defined host name.
                hostPortName - string - User defined host port name.
            hostPortSelectorByPortId :
                chassisIdSubtype - string - Value of chassisIdSubtype (encoding of 
                    chassisId) within LLDP data. Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
                chassisId - string - Value of chassisId within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorBySysName :
                sysName - string - Value of System Name within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorByPortSourceMAC :
                portSourceMAC - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    portSourceMAC.
    """
    plannedCapacity = kwargs.get('plannedCapacity', None)
    fiberConnectionMode = kwargs.get('fiberConnectionMode', None)
    requestedNominalPsdOffset = kwargs.get('requestedNominalPsdOffset', None)
    trafficMode = kwargs.get('trafficMode', None)
    fecIterations = kwargs.get('fecIterations', None)
    txCLPtarget = kwargs.get('txCLPtarget', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    hostPortName = kwargs.get('hostPortName', None)
    chassisId = kwargs.get('chassisId', None)
    moduleName = kwargs.get('moduleName', None)
    portSourceMAC = kwargs.get('portSourceMAC', None)
    moduleId = kwargs.get('moduleId', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    portId = kwargs.get('portId', None)
    portIdSubtype = kwargs.get('portIdSubtype', None)
    sysName = kwargs.get('sysName', None)
    hostName = kwargs.get('hostName', None)

    data = {
        "selector": {
            "moduleSelectorByModuleId": {
                "moduleId": moduleId
            },
            "moduleSelectorByModuleName": {
                "moduleName": moduleName
            },
            "moduleSelectorByModuleMAC": {
                "moduleMAC": moduleMAC
            },
            "moduleSelectorByModuleSerialNumber": {
                "moduleSerialNumber": moduleSerialNumber
            },
            "hostPortSelectorByName": {
                "hostName": hostName,
                "hostPortName": hostPortName
            },
            "hostPortSelectorByPortId": {
                "chassisIdSubtype": chassisIdSubtype,
                "chassisId": chassisId,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorBySysName": {
                "sysName": sysName,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorByPortSourceMAC": {
                "portSourceMAC": portSourceMAC
            }
        },
        "module": {
            "plannedCapacity": plannedCapacity,
            "fiberConnectionMode": fiberConnectionMode,
            "requestedNominalPsdOffset": requestedNominalPsdOffset,
            "trafficMode": trafficMode,
            "fecIterations": fecIterations,
            "txCLPtarget": txCLPtarget
        }
    }

    data = xrutils.selector_parse(data, selector)
    return data


def create_xr_networks(handle, **kwargs):
    """
    **Summary**
        ::
            Create xr-network
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param constellationFrequency: Carrier center frequency of the Hub module within the constellation (applied to Hub and leaf modules).
        :type constellationFrequency: integer
    
    **Optional Parameters**
        :name: string - User defined xr-network name
        :modulation: string - Constellation carrier signal modulation (applied to Hub and leaf modules).
            Possible values: '16QAM', 'QPSK' ' 8QAM'
             Possible Values: 16QAM, QPSK, 8QAM
        :tcMode: boolean - Enable/Disable IEEE 1588 Transparent Clock for VTI-mode.
            - true: Enabled
            - false: Disabled
            
        :topology: string - Indicates allowed connectivity configurations.
            Applicable only to Hub module (leaf modules value is always set to 'Auto')
            Possible values:
            - `auto` - Module allows configuration of both P2P and P2MP  connectivity.
            - `p2mp` - Module only allows configuration of P2MP connectivity.
             Possible Values: auto, p2mp
        :hubModule: object - Sourced from build_hubModule
        :leafModules: object - Sourced from build_leafModule
    """
    name = kwargs.get('name', None)
    constellationFrequency = kwargs.get('constellationFrequency', None)
    modulation = kwargs.get('modulation', None)
    tcMode = kwargs.get('tcMode', None)
    topology = kwargs.get('topology', None)
    hubModule = kwargs.get('hubModule', None)
    leafModules = kwargs.get('leafModules', None)

    request = [
        {
            "config": {
                "name": name,
                "constellationFrequency": constellationFrequency,
                "modulation": modulation,
                "tcMode": tcMode,
                "topology": topology
            },
            "hubModule": hubModule,
            "leafModules": leafModules
        }
    ]

    response = xrutils.send_request(handle, "POST", f"/api/v1/xr-networks", request_body=request)
    return response


def get_xr_networks_by_networkId(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific xr-network data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/xr-networks/{networkId}", q_value=q)
    return response


def update_xr_networks(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            Update xr-network
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
    
    **Optional Parameters**
        :name: string - User defined xr-network name
        :constellationFrequency: integer - Carrier center frequency of the Hub module within the constellation (applied to Hub and leaf modules).
        :modulation: string - Constellation carrier signal modulation (applied to Hub and leaf modules).
            Possible values: '16QAM', 'QPSK' ' 8QAM'
             Possible Values: 16QAM, QPSK, 8QAM
        :tcMode: boolean - Enable/Disable IEEE 1588 Transparent Clock for VTI-mode.
            - true: Enabled
            - false: Disabled
            
        :topology: string - Indicates allowed connectivity configurations.
            Applicable only to Hub module (leaf modules value is always set to 'Auto')
            Possible values:
            - `auto` - Module allows configuration of both P2P and P2MP  connectivity.
            - `p2mp` - Module only allows configuration of P2MP connectivity.
             Possible Values: auto, p2mp
        :managedBy: string - Indicates whether orchestration should be done through CM interface or through Host interface
            Possible values: 'host', 'cm'
            - 'host': Managed through host interface and discovered by CM
                      Cannot be edited or deleted through CM interface
            - 'cm': Managed through CM interface
                    Can be edited or deleted through CM interface
             Possible Values: host, cm
    """
    name = kwargs.get('name', None)
    constellationFrequency = kwargs.get('constellationFrequency', None)
    modulation = kwargs.get('modulation', None)
    tcMode = kwargs.get('tcMode', None)
    topology = kwargs.get('topology', None)
    managedBy = kwargs.get('managedBy', None)

    request = {
        "name": name,
        "constellationFrequency": constellationFrequency,
        "modulation": modulation,
        "tcMode": tcMode,
        "topology": topology,
        "managedBy": managedBy
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/xr-networks/{networkId}")
    return response


def delete_xr_networks(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            delete specific xr-network
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/xr-networks/{networkId}")
    return response


def get_xr_networks_hubModule(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            Retrieve xr-network hub info
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/xr-networks/{networkId}/hubModule", q_value=q)
    return response


def update_xr_networks_hubModule(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            Update hub module constellation parameters
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
    
    **Optional Parameters**
        :managedBy: string - Indicates whether orchestration should be done through CM interface or through Host interface
            Possible values: 'host', 'cm'
            - 'host': Managed through host interface and discovered by CM
                      Cannot be edited or deleted through CM interface
            - 'cm': Managed through CM interface
                    Can be edited or deleted through CM interface
             Possible Values: host, cm
        :plannedCapacity: string - Module planned capacity.
            Default and possible values are dependent of module type, capabilities, fiber connection mode and carrier modulation.
             Possible Values: 400G, 200G, 100G, 50G, 25G
        :fiberConnectionMode: string - Possible Values:
            - single: only one fiber is connected for by-directional traffic
            - dual: separate fibers for transmit and receive
            
        :requestedNominalPsdOffset: string - Requested Nominal PSD Offset
            This parameter is used to calculate the module's maxTxDSC
             Possible Values: 0dB, +3dB, +6dB
        :trafficMode: string - Possible Values:
            - L1Mode: Allows transparent transport of client traffic between XR hub and leaf module client ports
            - VTIMode: Allows transport of VLAN flows between an XR hub module client port to 1 or more XR leaf module client ports
            
        :fecIterations: string - FEC iterations.
            Possible values:
            - undefined
            - standard      Standard is 2 FEC iterations.
            - turbo         Turbo is 3 FEC iterations.
             Possible Values: undefined, standard, turbo
        :txCLPtarget: integer - Tx Carrier Launch Target Power in hundreds of dBm.
            Possible values:
            - Minimum: -3600
            - Maximum: 300
              Or
            - Value '-99.00': used for "Undefined".
            
    """
    managedBy = kwargs.get('managedBy', None)
    plannedCapacity = kwargs.get('plannedCapacity', None)
    fiberConnectionMode = kwargs.get('fiberConnectionMode', None)
    requestedNominalPsdOffset = kwargs.get('requestedNominalPsdOffset', None)
    trafficMode = kwargs.get('trafficMode', None)
    fecIterations = kwargs.get('fecIterations', None)
    txCLPtarget = kwargs.get('txCLPtarget', None)

    request = {
        "module": {
            "managedBy": managedBy,
            "plannedCapacity": plannedCapacity,
            "fiberConnectionMode": fiberConnectionMode,
            "requestedNominalPsdOffset": requestedNominalPsdOffset,
            "trafficMode": trafficMode,
            "fecIterations": fecIterations,
            "txCLPtarget": txCLPtarget
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/xr-networks/{networkId}/hubModule")
    return response


def get_xr_networks_leafModules(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            Retrieve xr-network leaf modules
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/xr-networks/{networkId}/leafModules", q_value=q)
    return response


def create_xr_networks_leafModules(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            Add xr-network leaf modules
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
        :param trafficMode: Possible Values:
            - L1Mode: Allows transparent transport of client traffic between XR hub and leaf module client ports
            - VTIMode: Allows transport of VLAN flows between an XR hub module client port to 1 or more XR leaf module client ports
            
        :type trafficMode: string
    
    **Optional Parameters**
        :plannedCapacity: string - Module planned capacity.
            Default and possible values are dependent of module type, capabilities, fiber connection mode and carrier modulation.
             Possible Values: 400G, 200G, 100G, 50G, 25G
        :fiberConnectionMode: string - Possible Values:
            - single: only one fiber is connected for by-directional traffic
            - dual: separate fibers for transmit and receive
            
        :requestedNominalPsdOffset: string - Requested Nominal PSD Offset
            This parameter is used to calculate the module's maxTxDSC
             Possible Values: 0dB, +3dB, +6dB
        :fecIterations: string - FEC iterations.
            Possible values:
            - undefined
            - standard      Standard is 2 FEC iterations.
            - turbo         Turbo is 3 FEC iterations.
             Possible Values: undefined, standard, turbo
        :txCLPtarget: integer - Tx Carrier Launch Target Power in hundreds of dBm.
            Possible values:
            - Minimum: -3600
            - Maximum: 300
              Or
            - Value '-99.00': used for "Undefined".
            
        :selector:
            moduleSelectorByModuleId :
                :moduleId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules using moduleId.
                
            moduleSelectorByModuleName :
                :moduleName: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
            moduleSelectorByModuleMAC :
                :moduleMAC: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
            moduleSelectorByModuleSerialNumber :
                :moduleSerialNumber: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
            hostPortSelectorByName :
                :hostName: string - User defined host name.
                
                :hostPortName: string - User defined host port name.
                
            hostPortSelectorByPortId :
                :chassisIdSubtype: string - Value of chassisIdSubtype (encoding of chassisId) within LLDP data.
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :chassisId: string - Value of chassisId within LLDP data
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :portIdSubtype: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
                :portId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
            hostPortSelectorBySysName :
                :sysName: string - Value of System Name within LLDP data
                Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria when associating discovered XR modules.
                
                :portIdSubtype: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
                :portId: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                
            hostPortSelectorByPortSourceMAC :
                :portSourceMAC: string - Only applicable when pre-planning objects.
                If defined, this parameter is used as matching criteria for associating the host port to a module client interface using the portSourceMAC.
                
    """
    plannedCapacity = kwargs.get('plannedCapacity', None)
    fiberConnectionMode = kwargs.get('fiberConnectionMode', None)
    requestedNominalPsdOffset = kwargs.get('requestedNominalPsdOffset', None)
    trafficMode = kwargs.get('trafficMode', None)
    fecIterations = kwargs.get('fecIterations', None)
    txCLPtarget = kwargs.get('txCLPtarget', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    hostPortName = kwargs.get('hostPortName', None)
    chassisId = kwargs.get('chassisId', None)
    moduleName = kwargs.get('moduleName', None)
    portSourceMAC = kwargs.get('portSourceMAC', None)
    moduleId = kwargs.get('moduleId', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    portId = kwargs.get('portId', None)
    portIdSubtype = kwargs.get('portIdSubtype', None)
    sysName = kwargs.get('sysName', None)
    hostName = kwargs.get('hostName', None)

    request = [
        {
            "selector": {
                "moduleSelectorByModuleId": {
                    "moduleId": moduleId
                },
                "moduleSelectorByModuleName": {
                    "moduleName": moduleName
                },
                "moduleSelectorByModuleMAC": {
                    "moduleMAC": moduleMAC
                },
                "moduleSelectorByModuleSerialNumber": {
                    "moduleSerialNumber": moduleSerialNumber
                },
                "hostPortSelectorByName": {
                    "hostName": hostName,
                    "hostPortName": hostPortName
                },
                "hostPortSelectorByPortId": {
                    "chassisIdSubtype": chassisIdSubtype,
                    "chassisId": chassisId,
                    "portIdSubtype": portIdSubtype,
                    "portId": portId
                },
                "hostPortSelectorBySysName": {
                    "sysName": sysName,
                    "portIdSubtype": portIdSubtype,
                    "portId": portId
                },
                "hostPortSelectorByPortSourceMAC": {
                    "portSourceMAC": portSourceMAC
                }
            },
            "module": {
                "plannedCapacity": plannedCapacity,
                "fiberConnectionMode": fiberConnectionMode,
                "requestedNominalPsdOffset": requestedNominalPsdOffset,
                "trafficMode": trafficMode,
                "fecIterations": fecIterations,
                "txCLPtarget": txCLPtarget
            }
        }
    ]

    request = xrutils.selector_parse(request, selector)
    response = xrutils.send_request(handle, "POST", f"/api/v1/xr-networks/{networkId}/leafModules", request_body=request)
    return response


def get_xr_networks_leafModules_by_nodeId(handle, networkId, nodeId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific xr-network leaf module data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
        :param nodeId: Index of leaf module into xr-network list
        :type nodeId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/xr-networks/{networkId}/leafModules/{nodeId}", q_value=q)
    return response


def update_xr_networks_leafModules(handle, networkId, nodeId, **kwargs):
    """
    **Summary**
        ::
            Update leaf module constellation parameters
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
        :param nodeId: Index of leaf module into xr-network list
        :type nodeId: string
    
    
    **Optional Parameters**
        :managedBy: string - Indicates whether orchestration should be done through CM interface or through Host interface
            Possible values: 'host', 'cm'
            - 'host': Managed through host interface and discovered by CM
                      Cannot be edited or deleted through CM interface
            - 'cm': Managed through CM interface
                    Can be edited or deleted through CM interface
             Possible Values: host, cm
        :plannedCapacity: string - Module planned capacity.
            Default and possible values are dependent of module type, capabilities, fiber connection mode and carrier modulation.
             Possible Values: 400G, 200G, 100G, 50G, 25G
        :fiberConnectionMode: string - Possible Values:
            - single: only one fiber is connected for by-directional traffic
            - dual: separate fibers for transmit and receive
            
        :requestedNominalPsdOffset: string - Requested Nominal PSD Offset
            This parameter is used to calculate the module's maxTxDSC
             Possible Values: 0dB, +3dB, +6dB
        :trafficMode: string - Possible Values:
            - L1Mode: Allows transparent transport of client traffic between XR hub and leaf module client ports
            - VTIMode: Allows transport of VLAN flows between an XR hub module client port to 1 or more XR leaf module client ports
            
        :fecIterations: string - FEC iterations.
            Possible values:
            - undefined
            - standard      Standard is 2 FEC iterations.
            - turbo         Turbo is 3 FEC iterations.
             Possible Values: undefined, standard, turbo
        :txCLPtarget: integer - Tx Carrier Launch Target Power in hundreds of dBm.
            Possible values:
            - Minimum: -3600
            - Maximum: 300
              Or
            - Value '-99.00': used for "Undefined".
            
    """
    managedBy = kwargs.get('managedBy', None)
    plannedCapacity = kwargs.get('plannedCapacity', None)
    fiberConnectionMode = kwargs.get('fiberConnectionMode', None)
    requestedNominalPsdOffset = kwargs.get('requestedNominalPsdOffset', None)
    trafficMode = kwargs.get('trafficMode', None)
    fecIterations = kwargs.get('fecIterations', None)
    txCLPtarget = kwargs.get('txCLPtarget', None)

    request = {
        "module": {
            "managedBy": managedBy,
            "plannedCapacity": plannedCapacity,
            "fiberConnectionMode": fiberConnectionMode,
            "requestedNominalPsdOffset": requestedNominalPsdOffset,
            "trafficMode": trafficMode,
            "fecIterations": fecIterations,
            "txCLPtarget": txCLPtarget
        }
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/xr-networks/{networkId}/leafModules/{nodeId}")
    return response


def delete_xr_networks_leafModules(handle, networkId, nodeId, **kwargs):
    """
    **Summary**
        ::
            delete specific xr-network leaf module
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
        :param nodeId: Index of leaf module into xr-network list
        :type nodeId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/xr-networks/{networkId}/leafModules/{nodeId}")
    return response


def get_xr_networks_reachableModules(handle, networkId, **kwargs):
    """
    **Summary**
        ::
            Retrieve xr-network reachableModules
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/xr-networks/{networkId}/reachableModules", q_value=q)
    return response


def get_xr_networks_reachableModules_by_nodeId(handle, networkId, nodeId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific xr-network reachableModule data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param networkId: Index into the xr-network list
        :type networkId: string
        :param nodeId: Index of leaf module into xr-network list
        :type nodeId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/xr-networks/{networkId}/reachableModules/{nodeId}", q_value=q)
    return response


def get_sw_actions(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of software control action objects
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/actions", q_value=q)
    return response


def build_sw_operation(handle, **kwargs):
    """
    **Summary**
        ::
            Helper method for create_sw_actions

        :param handle: xrctrl connection handle
        :type handle: string
        :param deviceType: Device type
            Possible values:
            - 'ndu'
            - 'moduleCfp2Dco
            - 'moduleQsfpDd'
            - 'moduleUnknown
             Possible Values: ndu, moduleCfp2Dco, moduleQsfpDd, moduleUnknown
        :type deviceType: string
        :param swURL: Source of software package for download to upgrade bank.
        :type swURL: string
    
    **Optional Parameters**
        :bankId: integer - Software bank colId.
        :prepareUpgrade: boolean - Operation to classify the upgrade impact (i.e., the impact of executing the software in the upgrade bank).
            Result is available on upgradeClassification property of the respective module swCtrl object.
             Possible Values: True
        :option: string - Activate operation options.
            Possible values:
            - 'apply': Activation is done over the upgrade bank image and is committed upon successful module restart.
            - 'rollback': Activation is done over the previous active bank image and no commit is issue upon module restart.
             Possible Values: apply, rollback
        :abort: boolean - Operation to abort module current action (if any) and clear pending operations. Possible Values: True
    """
    bankId = kwargs.get('bankId', None)
    deviceType = kwargs.get('deviceType', None)
    swURL = kwargs.get('swURL', None)
    prepareUpgrade = kwargs.get('prepareUpgrade', None)
    option = kwargs.get('option', None)
    abort = kwargs.get('abort', None)

    data = {
        "clearBank": {
            "bankId": bankId
        },
        "validateUrl": [
            {
                "deviceType": deviceType,
                "swURL": swURL
            }
        ],
        "download": [
            {
                "deviceType": deviceType,
                "swURL": swURL
            }
        ],
        "prepareUpgrade": prepareUpgrade,
        "activate": {
            "option": option
        },
        "abort": abort
    }

    return data


def create_sw_actions(handle, **kwargs):
    """
    **Summary**
        ::
            Create software control actions
    
        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :moduleIds: array - List of module ids to which the action should be applied.
        :nduIds: array - List of NDU ids to which the action should be applied.
        :xr_networkIds: array - List of xr-network ids to which the action should be applied.
            The list of module ids matching the xr-network is later displayed in the matchSelector state property.
            When executing an activate action for xr-network modules, IPM ensures that the "execute" moduleAction is finished on all xr-network modules before issuing the "commitSwImage".
            
        :operations: object - Sourced from build_sw_operation
    """
    name = kwargs.get('name', None)
    moduleIds = kwargs.get('moduleIds', None)
    nduIds = kwargs.get('nduIds', None)
    xr_networkIds = kwargs.get('xr_networkIds', None)
    operations = kwargs.get('operations', None)

    request = [
        {
            "name": name,
            "selectors": [
                {
                    "moduleIds": moduleIds,
                    "nduIds": nduIds,
                    "xr-networkIds": xr_networkIds
                }
            ],
            "operations": operations
        }
    ]

    response = xrutils.send_request(handle, "POST", f"/api/v1/sw/actions", request_body=request)
    return response


def get_sw_actions_by_actionId(handle, actionId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific software control action data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param actionId: Software control action identifier within the sw action list
        :type actionId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/actions/{actionId}", q_value=q)
    return response


def get_sw_moduleActions(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of module software control actions of an action request
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/moduleActions/", q_value=q)
    return response


def get_sw_moduleActions_by_moduleActionId(handle, moduleActionId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific module software control action data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param moduleActionId: Software control action identifier within the module sw action list
        :type moduleActionId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/moduleActions/{moduleActionId}", q_value=q)
    return response


def get_sw_inventory_ctrl(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all XR module SW images
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/inventory/ctrl", q_value=q)
    return response


def get_sw_inventory_device_ctrl(handle, deviceId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific software control object data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param deviceId: Device identifier (XR pluggable module or NDU).
        :type deviceId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/inventory/device/{deviceId}/ctrl", q_value=q)
    return response


def get_sw_inventory_device_swBanks(handle, deviceId, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all software banks in a XR pluggable module or ndu device
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param deviceId: Device identifier (XR pluggable module or NDU).
        :type deviceId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/inventory/device/{deviceId}/swBanks", q_value=q)
    return response


def get_sw_inventory_device_swBanks_by_swBankColId(handle, deviceId, swBankColId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific software bank data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param deviceId: Device identifier (XR pluggable module or NDU).
        :type deviceId: string
        :param swBankColId: Software bank identifier within module.
- '1': Refers to Bank A
- '2': Refers to Bank B

        :type swBankColId: integer
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/sw/inventory/device/{deviceId}/swBanks/{swBankColId}", q_value=q)
    return response


def get_transport_capacities(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all transport-capacity services
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/transport-capacities", q_value=q)
    return response


def build_tc_endpoint(handle, **kwargs):
    """
    **Summary**
        ::
            Helper method for create_transport_capacities

        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :capacity: integer - Client to network capacity of the infrastructure connection dscg Possible Values: 25, 50, 100, 200, 300, 400
    **Selector**
        :param selector: - 
            hostPortSelectorByName :
                hostName - string - User defined host name.
                hostPortName - string - User defined host port name.
            hostPortSelectorByPortId :
                chassisIdSubtype - string - Value of chassisIdSubtype (encoding of 
                    chassisId) within LLDP data. Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
                chassisId - string - Value of chassisId within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorBySysName :
                sysName - string - Value of System Name within LLDP data Only 
                    applicable when pre-planning objects. If defined, this parameter is 
                    used as matching criteria when associating discovered XR modules.
                portIdSubtype - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    tuple chassisIdSubtype, chassisId, portIdSubtype, portId.
                portId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria for associating 
                    the host port to a module client interface using the tuple 
                    chassisIdSubtype, chassisId, portIdSubtype, portId.
            hostPortSelectorByPortSourceMAC :
                portSourceMAC - string - Only applicable when pre-planning objects. 
                    If defined, this parameter is used as matching criteria for 
                    associating the host port to a module client interface using the 
                    portSourceMAC.
            moduleIfSelectorByModuleId :
                moduleId - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules using moduleId.
                moduleClientIfAid - string - TODO
            moduleIfSelectorByModuleName :
                moduleName - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
                moduleClientIfAid - string - TODO
            moduleIfSelectorByModuleMAC :
                moduleMAC - string - Only applicable when pre-planning objects. If 
                    defined, this parameter is used as matching criteria when 
                    associating discovered XR modules.
                moduleClientIfAid - string - TODO
            moduleIfSelectorByModuleSerialNumber :
                moduleSerialNumber - string - Only applicable when pre-planning 
                    objects. If defined, this parameter is used as matching criteria 
                    when associating discovered XR modules.
                moduleClientIfAid - string - TODO
    """
    capacity = kwargs.get('capacity', None)
    selector = kwargs.get('selector', None)
    moduleMAC = kwargs.get('moduleMAC', None)
    moduleSerialNumber = kwargs.get('moduleSerialNumber', None)
    hostPortName = kwargs.get('hostPortName', None)
    chassisId = kwargs.get('chassisId', None)
    portSourceMAC = kwargs.get('portSourceMAC', None)
    moduleName = kwargs.get('moduleName', None)
    moduleClientIfAid = kwargs.get('moduleClientIfAid', None)
    chassisIdSubtype = kwargs.get('chassisIdSubtype', None)
    moduleId = kwargs.get('moduleId', None)
    portId = kwargs.get('portId', None)
    portIdSubtype = kwargs.get('portIdSubtype', None)
    sysName = kwargs.get('sysName', None)
    hostName = kwargs.get('hostName', None)

    data = {
        "capacity": capacity,
        "selector": {
            "hostPortSelectorByName": {
                "hostName": hostName,
                "hostPortName": hostPortName
            },
            "hostPortSelectorByPortId": {
                "chassisIdSubtype": chassisIdSubtype,
                "chassisId": chassisId,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorBySysName": {
                "sysName": sysName,
                "portIdSubtype": portIdSubtype,
                "portId": portId
            },
            "hostPortSelectorByPortSourceMAC": {
                "portSourceMAC": portSourceMAC
            },
            "moduleIfSelectorByModuleId": {
                "moduleId": moduleId,
                "moduleClientIfAid": moduleClientIfAid
            },
            "moduleIfSelectorByModuleName": {
                "moduleName": moduleName,
                "moduleClientIfAid": moduleClientIfAid
            },
            "moduleIfSelectorByModuleMAC": {
                "moduleMAC": moduleMAC,
                "moduleClientIfAid": moduleClientIfAid
            },
            "moduleIfSelectorByModuleSerialNumber": {
                "moduleSerialNumber": moduleSerialNumber,
                "moduleClientIfAid": moduleClientIfAid
            }
        }
    }

    data = xrutils.selector_parse(data, selector)
    return data


def create_transport_capacities(handle, **kwargs):
    """
    **Summary**
        ::
            Create transport-capacity services
    
        :param handle: xrctrl connection handle
        :type handle: string
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :capacityMode: string - Defines the traffic characteristics of the transport capacity service.
            Possible values:
            - 'portMode': Provides transparent transport between XR hub and leaf modules
            - 'dedicatedDownlinkSymmetric': VLAN based P2P bidirectional flow between Hub and a Leaf modules with symmetric upstream and downstream bandwidths.
            - 'dedicatedDownlinkAsymmetric': VLAN based P2P bidirectional flow between Hub and a Leaf modules with asymmetric upstream and downstream bandwidths.
            - 'sharedDownlink': VLAN based bidirectional flow between Hub and Leaf modules where downstream traffic (hub to leaf) can be shared by multiple Leaf modules (as in a P2MP).
             Possible Values: portMode, dedicatedDownlinkSymmetric, dedicatedDownlinkAsymmetric, sharedDownlink
        :labels: object - Assign key:value labels to objects
        :endpoints: object - Sourced from build_tc_endpoint
    """
    name = kwargs.get('name', None)
    capacityMode = kwargs.get('capacityMode', None)
    labels = kwargs.get('labels', None)
    endpoints = kwargs.get('endpoints', None)

    request = [
        {
            "config": {
                "name": name,
                "capacityMode": capacityMode,
                "labels": labels
            },
            "endpoints": endpoints
        }
    ]

    response = xrutils.send_request(handle, "POST", f"/api/v1/transport-capacities", request_body=request)
    return response


def get_transport_capacities_by_tcId(handle, tcId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific transport-capacity data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param tcId: Index into the transport-connection list
        :type tcId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/transport-capacities/{tcId}", q_value=q)
    return response


def update_transport_capacities(handle, tcId, **kwargs):
    """
    **Summary**
        ::
            Update specific transport-capacity data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param tcId: Index into the transport-connection list
        :type tcId: string
    
    
    **Optional Parameters**
        :name: string - User defined object name.
            
        :labels: object - Assign key:value labels to objects
    """
    name = kwargs.get('name', None)
    labels = kwargs.get('labels', None)

    request = {
        "name": name,
        "labels": labels
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/transport-capacities/{tcId}")
    return response


def delete_transport_capacities(handle, tcId, **kwargs):
    """
    **Summary**
        ::
            Delete specific transport-capacity
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param tcId: Index into the transport-connection list
        :type tcId: string
    
    """

    response = xrutils.send_request(handle, "DELETE", f"/api/v1/transport-capacities/{tcId}")
    return response


def get_transport_capacities_endpoints(handle, tcId, **kwargs):
    """
    **Summary**
        ::
            Retrieve transport-capacity connection endpoints
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param tcId: Index into the transport-connection list
        :type tcId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/transport-capacities/{tcId}/endpoints", q_value=q)
    return response


def get_transport_capacities_endpoints_by_epId(handle, tcId, epId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific endpoint data from a transport-capacity connection
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param tcId: Index into the transport-connection list
        :type tcId: string
        :param epId: Endpoint identifier within the transport-connection
        :type epId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/transport-capacities/{tcId}/endpoints/{epId}", q_value=q)
    return response


def update_transport_capacities_endpoints(handle, tcId, epId, **kwargs):
    """
    **Summary**
        ::
            Update specific transport-capacity connection endpoint data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param tcId: Index into the transport-connection list
        :type tcId: string
        :param epId: Endpoint identifier within the transport-connection
        :type epId: string
    
        :param capacity: Client to network capacity of the infrastructure connection dscg Possible Values: 25, 50, 100, 200, 300, 400
        :type capacity: integer
    """
    capacity = kwargs.get('capacity', None)

    request = {
        "capacity": capacity
    }

    response = xrutils.send_request(handle, "PUT", f"/api/v1/transport-capacities/{tcId}/endpoints/{epId}")
    return response


def get_capacity_links(handle, **kwargs):
    """
    **Summary**
        ::
            Retrieve list of all capacity-links
    
        :param handle: xrctrl connection handle
        :type handle: string
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/capacity-links", q_value=q)
    return response


def get_capacity_links_by_clId(handle, clId, **kwargs):
    """
    **Summary**
        ::
            Retrieve specific capacity-link data
    
        :param handle: xrctrl connection handle
        :type handle: string
        :param clId: Index into the capacity-link list
        :type clId: string
    
    **Optional Parameters**
        :param q: Query Filter. Single-entry dictionary composed of: {attribute: value}
        :type q: dict
    """
    q = kwargs.get('q', None)

    response = xrutils.send_request(handle, "GET", f"/api/v1/capacity-links/{clId}", q_value=q)
    return response


