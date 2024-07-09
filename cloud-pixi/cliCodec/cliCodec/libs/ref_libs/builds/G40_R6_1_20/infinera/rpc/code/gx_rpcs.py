import gxutils
#
# auto-generated pixi build code file
# Build: G40_R6_1_20_IOA | Yang: infinera
#

def activate_file(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            filetype - str - Predefined filetype available for upload
            label - str - Label to be activated
            db_instance - str - Database instance name to activate.
            sanity_check_override - bool - Allows user to skip the 
                database/swimage sanity check.
            db_action - str - Specify the expected database operation during 
                activating software image.
            db_passphrase - str - Passphrase used for encrypting and decrypting 
                DB snapshots. For each command associated with DB snapshots (backup, 
                restore, etc), this db-passphrase will be used, except when it is 
                directly provided in each command. Automatic DB snapshots will not 
                be enabled until this parameter is set.

    ----------------------------
    """

    filetype = kwargs.get('filetype', None)
    label = kwargs.get('label', None)
    db_instance = kwargs.get('db_instance', None)
    sanity_check_override = kwargs.get('sanity_check_override', None)
    db_action = kwargs.get('db_action', None)
    db_passphrase = kwargs.get('db_passphrase', None)

    manager = kwargs.get('manager')

    request = {
        "filetype": filetype,
        "label": label,
        "db-instance": db_instance,
        "sanity-check-override": sanity_check_override,
        "db-action": db_action,
        "db-passphrase": db_passphrase
    }

    response = gxutils.send_rpc(manager, 'activate-file', request)
    return response


def activate_fw(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            fw_image_name - unknown - FW file name
            resource - str - List of equipment to be activated.

    ----------------------------
    """

    fw_image_name = kwargs.get('fw_image_name', None)
    resource = kwargs.get('resource', None)

    manager = kwargs.get('manager')

    request = {
        "fw-image-name": fw_image_name,
        "resource": resource
    }

    response = gxutils.send_rpc(manager, 'activate-fw', request)
    return response


def appctl(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            command - str - Application control commands.
            app_name - unknown - Third party app name.
            target - str - Entire system or chassis/card AID.
            parameters - str - Optional parameters to be passed in the command.

    ----------------------------
    """

    command = kwargs.get('command', None)
    app_name = kwargs.get('app_name', None)
    target = kwargs.get('target', None)
    parameters = kwargs.get('parameters', None)

    manager = kwargs.get('manager')

    request = {
        "command": command,
        "app-name": app_name,
        "target": target,
        "parameters": parameters
    }

    response = gxutils.send_rpc(manager, 'appctl', request)
    return response


def apply_template(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            template_type - str - The type of template to apply. Other 
                parameters may be required depending on the template type.
            applicable_tom - str - List of TOMs to which to apply 
                serdes-templates against. If not provided (e.g. list is empty), all 
                system TOMs will be considered for application.

    ----------------------------
    """

    template_type = kwargs.get('template_type', None)
    applicable_tom = kwargs.get('applicable_tom', None)

    manager = kwargs.get('manager')

    request = {
        "template-type": template_type,
        "applicable-tom": applicable_tom
    }

    response = gxutils.send_rpc(manager, 'apply-template', request)
    return response


def call_home(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            dial_out_server_name - unknown - The dial-out-server to connect to.

    ----------------------------
    """

    dial_out_server_name = kwargs.get('dial_out_server_name', None)

    manager = kwargs.get('manager')

    request = {
        "dial-out-server-name": dial_out_server_name
    }

    response = gxutils.send_rpc(manager, 'call-home', request)
    return response


def cancel_commit(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            persist_id - str - This parameter is given in order to cancel a 
                persistent confirmed commit. The value must be equal to the value 
                given in the 'persist' parameter to the <commit> operation. If it 
                does not match, the operation fails with an 'invalid-value' error.

    ----------------------------
    """

    persist_id = kwargs.get('persist_id', None)

    manager = kwargs.get('manager')

    request = {
        "persist-id": persist_id
    }

    response = gxutils.send_rpc(manager, 'cancel-commit', request)
    return response


def cancel_upgrade(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'cancel-upgrade', request)
    return response


def cert_gen(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            certificate_name - str - Specifies the name of the certificate to be 
                generated.
            days - int - Number of days a certificate is valid for.
            org_name - str - Organization Name.
            common_name - str - IP or hostname to identify the server.
            subject - str - The full certificate subject name
            auto_install - bool - Auto-assign certificate to any 
                secure-application without active certificate.

    ----------------------------
    """

    certificate_name = kwargs.get('certificate_name', None)
    days = kwargs.get('days', None)
    org_name = kwargs.get('org_name', None)
    common_name = kwargs.get('common_name', None)
    subject = kwargs.get('subject', None)
    auto_install = kwargs.get('auto_install', None)

    manager = kwargs.get('manager')

    request = {
        "certificate-name": certificate_name,
        "days": days,
        "org-name": org_name,
        "common-name": common_name,
        "subject": subject,
        "auto-install": auto_install
    }

    response = gxutils.send_rpc(manager, 'cert-gen', request)
    return response


def change_ztp_mode(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            ztp_mode - str - Selects new ztp mode.

    ----------------------------
    """

    ztp_mode = kwargs.get('ztp_mode', None)

    manager = kwargs.get('manager')

    request = {
        "ztp-mode": ztp_mode
    }

    response = gxutils.send_rpc(manager, 'change-ztp-mode', request)
    return response


def clear_alarm(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            alarm_type - unknown - Type of alarm to be cleared. Note: only some 
                alarms are eligible to be cleared using this operation; see 
                alarm-inventory/can-be-cleared-by-user for details.
            resource - unknown - Resource of alarm to be cleared. May be one or 
                more resources assocaited with the provided alarm-type.

    ----------------------------
    """

    alarm_type = kwargs.get('alarm_type', None)
    resource = kwargs.get('resource', None)

    manager = kwargs.get('manager')

    request = {
        "alarm-type": alarm_type,
        "resource": resource
    }

    response = gxutils.send_rpc(manager, 'clear-alarm', request)
    return response


def clear_app(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            app_name - unknown - Third party app name.

    ----------------------------
    """

    app_name = kwargs.get('app_name', None)

    manager = kwargs.get('manager')

    request = {
        "app-name": app_name
    }

    response = gxutils.send_rpc(manager, 'clear-app', request)
    return response


def clear_certificate(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            type - str - Defines the type of 'clear certificate' that the system 
                must do.
            id - str - Foreign Key pointing to the id of the certificate to 
                delete.

    ----------------------------
    """

    type = kwargs.get('type', None)
    id = kwargs.get('id', None)

    manager = kwargs.get('manager')

    request = {
        "type": type,
        "id": id
    }

    response = gxutils.send_rpc(manager, 'clear-certificate', request)
    return response


def clear_crl(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            clear_target - str - Defines the target CRL(s) of the clear operation.
            crl_name - unknown - Name of the CRL to delete.

    ----------------------------
    """

    clear_target = kwargs.get('clear_target', None)
    crl_name = kwargs.get('crl_name', None)

    manager = kwargs.get('manager')

    request = {
        "clear-target": clear_target,
        "crl-name": crl_name
    }

    response = gxutils.send_rpc(manager, 'clear-crl', request)
    return response


def clear_database(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            clear_type - str - Defines the type of 'clear database' that the 
                system must do.

    ----------------------------
    """

    clear_type = kwargs.get('clear_type', None)

    manager = kwargs.get('manager')

    request = {
        "clear-type": clear_type
    }

    response = gxutils.send_rpc(manager, 'clear-database', request)
    return response


def clear_diagnostics(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            entity_id - str - Target entity for the command. Must exist.
            test_signal_direction - str - The test signal direction. If not 
                specified, the counter for the enabled direction would be cleared.

    ----------------------------
    """

    entity_id = kwargs.get('entity_id', None)
    test_signal_direction = kwargs.get('test_signal_direction', None)

    manager = kwargs.get('manager')

    request = {
        "entity-id": entity_id,
        "test-signal-direction": test_signal_direction
    }

    response = gxutils.send_rpc(manager, 'clear-diagnostics', request)
    return response


def clear_file(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            filetype - str - Predefined filetype available for clearing the file
            target_file - str - Filepath of the file to be deleted

    ----------------------------
    """

    filetype = kwargs.get('filetype', None)
    target_file = kwargs.get('target_file', None)

    manager = kwargs.get('manager')

    request = {
        "filetype": filetype,
        "target-file": target_file
    }

    response = gxutils.send_rpc(manager, 'clear-file', request)
    return response


def clear_log(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            log_file_name - unknown - The log file to clear; file will still 
                exist, but with empty content.

    ----------------------------
    """

    log_file_name = kwargs.get('log_file_name', None)

    manager = kwargs.get('manager')

    request = {
        "log-file-name": log_file_name
    }

    response = gxutils.send_rpc(manager, 'clear-log', request)
    return response


def clear_ospf_instance(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            instance - unknown - OSPF protocol instance which need to be 
                re-started.

    ----------------------------
    """

    instance = kwargs.get('instance', None)

    manager = kwargs.get('manager')

    request = {
        "instance": instance
    }

    response = gxutils.send_rpc(manager, 'clear-ospf-instance', request)
    return response


def clear_pm(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            data_type - str - Type of PM data to clear.
            period - str - Time period for PM data.
            direction - str - PM parameter direction.
            location - str - PM parameter location.
            resource - str - Existing system resource.
            resource_type - str - Type of resource.
            AID - str - Resource Access Identifier (AID). Identifies an instance 
                within a specific resource type.

    ----------------------------
    """

    data_type = kwargs.get('data_type', None)
    period = kwargs.get('period', None)
    direction = kwargs.get('direction', None)
    location = kwargs.get('location', None)
    resource = kwargs.get('resource', None)
    resource_type = kwargs.get('resource_type', None)
    AID = kwargs.get('AID', None)

    manager = kwargs.get('manager')

    request = {
        "data-type": data_type,
        "period": period,
        "direction": direction,
        "location": location,
        "resource": resource,
        "resource-type": resource_type,
        "AID": AID
    }

    response = gxutils.send_rpc(manager, 'clear-pm', request)
    return response


def clear_recover_mode(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'clear-recover-mode', request)
    return response


def clear_system(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            type - str - Clear system type.
            target - str - Entire system (main controller chassis) or specific 
                chassis/card AID.
            restart_behavior - str - Action to do after the clean operation.
            action - str - Action to clean the partition.

    ----------------------------
    """

    type = kwargs.get('type', None)
    target = kwargs.get('target', None)
    restart_behavior = kwargs.get('restart_behavior', None)
    action = kwargs.get('action', None)

    manager = kwargs.get('manager')

    request = {
        "type": type,
        "target": target,
        "restart-behavior": restart_behavior,
        "action": action
    }

    response = gxutils.send_rpc(manager, 'clear-system', request)
    return response


def clear_topology(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            target - str - Target instance to be cleared. May be a 
                lldp-neighbor, a carrier-neighbor or a lldp-port-statistics instance.

    ----------------------------
    """

    target = kwargs.get('target', None)

    manager = kwargs.get('manager')

    request = {
        "target": target
    }

    response = gxutils.send_rpc(manager, 'clear-topology', request)
    return response


def cli_command(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            echo - str - If echo on, result includes commands and their output; 
                otherwise it will only include the commands output
            error_option - str - How the command execution should behave when 
                errors occur.
            replace - bool - If true, it tries to push the entire 
                script/commands as a replace operation
            script_file - str - The filepath of the previously downloaded CLI 
                script
            commands - str - CLI commands to execute; multiple commands can be 
                provided, one per line

    ----------------------------
    """

    echo = kwargs.get('echo', None)
    error_option = kwargs.get('error_option', None)
    replace = kwargs.get('replace', None)
    script_file = kwargs.get('script_file', None)
    commands = kwargs.get('commands', None)

    manager = kwargs.get('manager')

    request = {
        "echo": echo,
        "error-option": error_option,
        "replace": replace,
        "script-file": script_file,
        "commands": commands
    }

    response = gxutils.send_rpc(manager, 'cli-command', request)
    print("Response: " + str(response))
    return response


def close_session(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'close-session', request)
    return response


def commit(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            confirmed - str - Requests a confirmed commit.
            confirm_timeout - int - The timeout interval for a confirmed commit.
            persist - str - This parameter is used to make a confirmed commit 
                persistent. A persistent confirmed commit is not aborted if the 
                NETCONF session terminates. The only way to abort a persistent 
                confirmed commit is to let the timer expire, or to use the 
                <cancel-commit> operation. The value of this parameter is a token 
                that must be given in the 'persist-id' parameter of <commit> or 
                <cancel-commit> operations in order to confirm or cancel the 
                persistent confirmed commit. The token should be a random string.
            persist_id - str - This parameter is given in order to commit a 
                persistent confirmed commit. The value must be equal to the value 
                given in the 'persist' parameter to the <commit> operation. If it 
                does not match, the operation fails with an 'invalid-value' error.

    ----------------------------
    """

    confirmed = kwargs.get('confirmed', None)
    confirm_timeout = kwargs.get('confirm_timeout', None)
    persist = kwargs.get('persist', None)
    persist_id = kwargs.get('persist_id', None)

    manager = kwargs.get('manager')

    request = {
        "confirmed": confirmed,
        "confirm-timeout": confirm_timeout,
        "persist": persist,
        "persist-id": persist_id
    }

    response = gxutils.send_rpc(manager, 'commit', request)
    return response


def copy_config(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'copy-config', request)
    return response


def create_subscription(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            stream - str - An optional parameter that indicates which stream of 
                events is of interest. If not present, then events in the default 
                NETCONF stream will be sent.
            startTime - str - A parameter used to trigger the replay feature and 
                indicates that the replay should start at the time specified. If 
                start time is not present, this is not a replay subscription.
            stopTime - str - An optional parameter used with the optional replay 
                feature to indicate the newest notifications of interest. If stop 
                time is not present, the notifications will continue until the 
                subscription is terminated. Must be used with startTime.

    ----------------------------
    """

    stream = kwargs.get('stream', None)
    startTime = kwargs.get('startTime', None)
    stopTime = kwargs.get('stopTime', None)

    manager = kwargs.get('manager')

    request = {
        "stream": stream,
        "startTime": startTime,
        "stopTime": stopTime
    }

    response = gxutils.send_rpc(manager, 'create-subscription', request)
    return response


def create_xcon(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            payload_type - str - Indicates a generic, high-level source (from) 
                client payload type of the digital XCON.
            direction - str - Indicates whether the digital XCON is 
                uni-directional (1-WAY) or bi-directional (2-WAY).
            circuit_id_suffix - str - User configured circuit ID suffix.
            label - str - User label.
            source - str - Source end-point of the xcon. Must be an existing 
                facility that can be used as a XCON end-point.
            src_parent_odu - str - Name of the High Order parent ODU where to 
                audst-create this ODU end-point.
            src_time_slots - str - List of time-slots to allocate to the 
                automatically created LO-ODU. Value can be: - omitted/empty - in 
                which case system will audst-allocate time-slots based on the 
                src-instance-id, which becomes mandatory (this is only supported for 
                non ODUflex scenarios.) - starting time-slot - system automatically 
                allocates the rest of the time-slots sequentially from this starting 
                point; will fail if those time-slots are not available - time-slot 
                list - full list of time-slots, using a comma separated list, with 
                'x..y' representing ranges; the total number of time-slots need to 
                match the associated payload-type (e.g. 80 time-slots for 100G 
                payload, 320 time-slots for 400G payload, etc)
            src_instance_id - int - Optional parameter on LO-ODU creation, 
                identifies the ODU within the parent/high-order ODU. If not 
                provided, it is automatically derived. Max value depends on capacity 
                of the HO-ODU and of the odu-type. (ex: for creating an ODU4 in a HO 
                ODUC8, instance can be between 1 and 8) Note: instance-id becomes 
                mandatory if time-slots are not provided.
            destination - str - Destination end-point of the xcon. Must be an 
                existing facility that can be used as a XCON end-point.
            dst_parent_odu - str - Name of the High Order parent ODU where to 
                audst-create this ODU end-point.
            dst_time_slots - str - List of time-slots to allocate to the 
                automatically created LO-ODU. Value can be: - omitted/empty - in 
                which case system will audst-allocate time-slots based on the 
                dst-instance-id, which becomes mandatory (this is only supported for 
                non ODUflex scenarios.) - starting time-slot - system automatically 
                allocates the rest of the time-slots sequentially from this starting 
                point; will fail if those time-slots are not available - time-slot 
                list - full list of time-slots, using a comma separated list, with 
                'x..y' representing ranges; the total number of time-slots need to 
                match the associated payload-type (e.g. 80 time-slots for 100G 
                payload, 320 time-slots for 400G payload, etc)
            dst_instance_id - int - Optional parameter on LO-ODU creation, 
                identifies the ODU within the parent/high-order ODU. If not 
                provided, it is automatically derived. Max value depends on capacity 
                of the HO-ODU and of the odu-type. (ex: for creating an ODU4 in a HO 
                ODUC8, instance can be between 1 and 8) Note: instance-id becomes 
                mandatory if time-slots are not provided.

    ----------------------------
    """

    payload_type = kwargs.get('payload_type', None)
    direction = kwargs.get('direction', None)
    circuit_id_suffix = kwargs.get('circuit_id_suffix', None)
    label = kwargs.get('label', None)
    source = kwargs.get('source', None)
    src_parent_odu = kwargs.get('src_parent_odu', None)
    src_time_slots = kwargs.get('src_time_slots', None)
    src_instance_id = kwargs.get('src_instance_id', None)
    destination = kwargs.get('destination', None)
    dst_parent_odu = kwargs.get('dst_parent_odu', None)
    dst_time_slots = kwargs.get('dst_time_slots', None)
    dst_instance_id = kwargs.get('dst_instance_id', None)

    manager = kwargs.get('manager')

    request = {
        "payload-type": payload_type,
        "direction": direction,
        "circuit-id-suffix": circuit_id_suffix,
        "label": label,
        "source": source,
        "src-parent-odu": src_parent_odu,
        "src-time-slots": src_time_slots,
        "src-instance-id": src_instance_id,
        "destination": destination,
        "dst-parent-odu": dst_parent_odu,
        "dst-time-slots": dst_time_slots,
        "dst-instance-id": dst_instance_id
    }

    response = gxutils.send_rpc(manager, 'create-xcon', request)
    return response


def csr_gen(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            certificate_name - str - Specifies the name of the certificate to be 
                generated. Using existing name implies rotation. NOTE: When 
                importing the signed certificate at a later step, the exact same 
                certificate-name needs to be used.
            signature_hash_algorithm - str - Hash algorithm to be used. Default 
                value depends on the selected key-algorithm.
            metadata_template - str - Selects the possible sources for the CSR 
                metadata, including reusing it from an existing certificate, loading 
                from an openssl cnf file, or using a generic template which defines 
                the metadata defaults. In all cases except for 'from-openssl-cnf', 
                it is possible to override the metadata individual parameters by 
                providing the metadata parameters (subject, SAN, etc) explicitly.
            metadata_from_certificate - unknown - A local-certificate id to be 
                used as metadata source. Metadata details can be overridden 
                separately.
            metadata_from_cnf - str - Multi-line string input of cnf with 
                metadata. Metadata details can be overridden separately.
            subject - str - The certificate subject. The common name (CN) RDN is 
                *mandatory*. Each relative DN must have a prefix slash (/). Example 
                a minimal valid subject (contains CN only): '/CN=Infinera' An 
                example with all supported RDN fields: 
                '/CN=InfineraRoot/C=US/ST=California/L=Sunnyvale/O=InfineraCorporation/OU=InfineraR&D'
                
            SAN - str - The certificate SAN (Subject Alternate Name) fields. 
                SANs are specified as Type-Value comma separated list. Valid types 
                are 'IP', 'DNS' and 'otherName'. Examples: 
                SAN='IP:127.0.0.1,DNS:localhost' 
                SAN='dns:GX-10-4,otherName:1.3.6.1.4.1.21296.1.2.2.1.2;UTF8:GX-10-4'
            key_usage - str - The Key Usage type(s) for the certificate. Default 
                is derived from the metadata-template parameter.
            extended_key_usage - str - The Extended Key Usage type(s) for the 
                certificate. Default is derived from the metadata-template parameter.
            key_algorithm - str - Specifies the algorithm to be used for a new 
                key pair for this CSR.
            key_from_certificate - unknown - Allows to reuse the key pair from 
                an existing local-certificate.

    ----------------------------
    """

    certificate_name = kwargs.get('certificate_name', None)
    signature_hash_algorithm = kwargs.get('signature_hash_algorithm', None)
    metadata_template = kwargs.get('metadata_template', None)
    metadata_from_certificate = kwargs.get('metadata_from_certificate', None)
    metadata_from_cnf = kwargs.get('metadata_from_cnf', None)
    subject = kwargs.get('subject', None)
    SAN = kwargs.get('SAN', None)
    key_usage = kwargs.get('key_usage', None)
    extended_key_usage = kwargs.get('extended_key_usage', None)
    key_algorithm = kwargs.get('key_algorithm', None)
    key_from_certificate = kwargs.get('key_from_certificate', None)

    manager = kwargs.get('manager')

    request = {
        "certificate-name": certificate_name,
        "signature-hash-algorithm": signature_hash_algorithm,
        "metadata-template": metadata_template,
        "metadata-from-certificate": metadata_from_certificate,
        "metadata-from-cnf": metadata_from_cnf,
        "subject": subject,
        "SAN": SAN,
        "key-usage": key_usage,
        "extended-key-usage": extended_key_usage,
        "key-algorithm": key_algorithm,
        "key-from-certificate": key_from_certificate
    }

    response = gxutils.send_rpc(manager, 'csr-gen', request)
    return response


def default(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            entity_id - str - Instances to be defaulted.
            attribute - str - Attribute names to be defaulted. If empty, default 
                all entities' attributes.

    ----------------------------
    """

    entity_id = kwargs.get('entity_id', None)
    attribute = kwargs.get('attribute', None)

    manager = kwargs.get('manager')

    request = {
        "entity-id": entity_id,
        "attribute": attribute
    }

    response = gxutils.send_rpc(manager, 'default', request)
    return response


def delete_config(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'delete-config', request)
    return response


def delete_isk(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            key_name - unknown - Image Signing Key (ISK) name

    ----------------------------
    """

    key_name = kwargs.get('key_name', None)

    manager = kwargs.get('manager')

    request = {
        "key-name": key_name
    }

    response = gxutils.send_rpc(manager, 'delete-isk', request)
    return response


def diff(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            candidate - str - The candidate datastore configuration.

    ----------------------------
    """

    candidate = kwargs.get('candidate', None)

    manager = kwargs.get('manager')

    request = {
        "candidate": candidate
    }

    response = gxutils.send_rpc(manager, 'diff', request)
    return response


def disable_led(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            entity - str - Targets a specific entity in the system for having 
                its location led test disabled. Can be a chassis or a card.

    ----------------------------
    """

    entity = kwargs.get('entity', None)

    manager = kwargs.get('manager')

    request = {
        "entity": entity
    }

    response = gxutils.send_rpc(manager, 'disable-led', request)
    return response


def discard_changes(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'discard-changes', request)
    return response


def display_cert(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            display_type - str - Defines the requested type of display operation.
            certificate - str - The target certificate to display details or 
                trust-chain.

    ----------------------------
    """

    display_type = kwargs.get('display_type', None)
    certificate = kwargs.get('certificate', None)

    manager = kwargs.get('manager')

    request = {
        "display-type": display_type,
        "certificate": certificate
    }

    response = gxutils.send_rpc(manager, 'display-cert', request)
    return response


def download(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            filetype - str - Predefined filetype available for download
            passphrase - str - To decode encrypted input files.
            white_listed - bool - If true, peer-certificate does not have an 
                associated trust-chain. Else, has an associated trust-chain.
            certificate_name - str - X509v3 local/trusted/peer certificate id.
            intermediate_import - bool - Allow to import any intermediate 
                certificates present in a certificate file bundle. If 
                certificate-name is not provided, it will be auto-generated from the 
                topmost certificate Issuer CN plus a numeric suffix.
            unattended - bool - Auto prepare and auto activate file after a 
                successful download. Only some files support 'activation'; others 
                just ignore this flag.
            async_ - bool - Download asynchronously.
            skip_secure_verification - bool - For HTTPS transfers, skip TLS 
                verification. For SCP/SFTP transfers, skip ssh known host checking. 
                If flag not set, verification is done according with current 
                security-policy.
            sanity_check_override - bool - If true, skips the sanity check 
                override when downloading a database snapshot.
            destination - str - Allows user to provide the destination for the 
                downloaded file, including directory and/or filename. This is only 
                applicable when file-type is 'file', representing a generic file 
                transfer. The parameter can be: - omitted: means file is downloaded 
                to the default directory with the original file-name - a file-name 
                only: uses default directory with the new file-name - a relative 
                path: uses the default directory as starting path, plus relative 
                path - an absolute path: Absolute path for the user accessible 
                directories can be used It is necessary for the user to have write 
                access to the destination path for the download to succeed. Tip: use 
                'show transfer' to see what is the default storage directory. For 
                generic file transfer, no further activity occurs after download, so 
                the 'unattended' flag will be ignored.
            password - str - SFTP/SCP/FTP/HTTP/HTTPS password
            db_passphrase - str - Passphrase used for encrypting and decrypting 
                DB snapshots. For each command associated with DB snapshots (backup, 
                restore, etc), this db-passphrase will be used, except when it is 
                directly provided in each command. Automatic DB snapshots will not 
                be enabled until this parameter is set.
            db_action - str - Specify the expected database operation during 
                activating software image.
            source - str - Source of the download 
                ([sftp|scp|http|https|ftp|file]://[user@]hostname/directorypath/filename)
                
            file_server - unknown - The preconfigured file-server name.
            path - str - Path (directory and filename) of the remote file.

    ----------------------------
    """

    filetype = kwargs.get('filetype', None)
    passphrase = kwargs.get('passphrase', None)
    white_listed = kwargs.get('white_listed', None)
    certificate_name = kwargs.get('certificate_name', None)
    intermediate_import = kwargs.get('intermediate_import', None)
    unattended = kwargs.get('unattended', None)
    async_ = kwargs.get('async_', None)
    skip_secure_verification = kwargs.get('skip_secure_verification', None)
    sanity_check_override = kwargs.get('sanity_check_override', None)
    destination = kwargs.get('destination', None)
    password = kwargs.get('password', None)
    db_passphrase = kwargs.get('db_passphrase', None)
    db_action = kwargs.get('db_action', None)
    source = kwargs.get('source', None)
    file_server = kwargs.get('file_server', None)
    path = kwargs.get('path', None)

    manager = kwargs.get('manager')

    request = {
        "filetype": filetype,
        "passphrase": passphrase,
        "white-listed": white_listed,
        "certificate-name": certificate_name,
        "intermediate-import": intermediate_import,
        "unattended": unattended,
        "async": async_,
        "skip-secure-verification": skip_secure_verification,
        "sanity-check-override": sanity_check_override,
        "destination": destination,
        "password": password,
        "db-passphrase": db_passphrase,
        "db-action": db_action,
        "source": source,
        "file-server": file_server,
        "path": path
    }

    response = gxutils.send_rpc(manager, 'download', request)
    return response


def edit_config(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            default_operation - str - The default operation to use.
            test_option - str - The test option to use.
            error_option - str - The error option to use.
            url - str - URL-based config content.

    ----------------------------
    """

    default_operation = kwargs.get('default_operation', None)
    test_option = kwargs.get('test_option', None)
    error_option = kwargs.get('error_option', None)
    url = kwargs.get('url', None)

    manager = kwargs.get('manager')

    request = {
        "default-operation": default_operation,
        "test-option": test_option,
        "error-option": error_option,
        "url": url
    }

    response = gxutils.send_rpc(manager, 'edit-config', request)
    return response


def enable_led(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            entity - str - Targets a specific entity in the system for enabling 
                its location led test. Can be a chassis or a card.
            timeout - int - Specify the timeout, in seconds, before enable-led 
                terminates. 0 means no timeout.
            led_mode - str - Selects the led flash pattern.

    ----------------------------
    """

    entity = kwargs.get('entity', None)
    timeout = kwargs.get('timeout', None)
    led_mode = kwargs.get('led_mode', None)

    manager = kwargs.get('manager')

    request = {
        "entity": entity,
        "timeout": timeout,
        "led-mode": led_mode
    }

    response = gxutils.send_rpc(manager, 'enable-led', request)
    return response


def file_operation(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            operation - str - File operations to do.
            file_path - str - Current file path.
            new_file_path - str - New file path.

    ----------------------------
    """

    operation = kwargs.get('operation', None)
    file_path = kwargs.get('file_path', None)
    new_file_path = kwargs.get('new_file_path', None)

    manager = kwargs.get('manager')

    request = {
        "operation": operation,
        "file-path": file_path,
        "new-file-path": new_file_path
    }

    response = gxutils.send_rpc(manager, 'file-operation', request)
    return response


def get_conditions(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            direction - str - Direction of the condition.
            location - str - Location of the condition.
            resource - str - Existing system resource.
            resource_type - str - Type of resource.
            AID - str - Resource Access Identifier (AID). Identifies an instance 
                within a specific resource type.
            alarm_type - str - Type of alarm, based on an abbreviated code.

    ----------------------------
    """

    direction = kwargs.get('direction', None)
    location = kwargs.get('location', None)
    resource = kwargs.get('resource', None)
    resource_type = kwargs.get('resource_type', None)
    AID = kwargs.get('AID', None)
    alarm_type = kwargs.get('alarm_type', None)

    manager = kwargs.get('manager')

    request = {
        "direction": direction,
        "location": location,
        "resource": resource,
        "resource-type": resource_type,
        "AID": AID,
        "alarm-type": alarm_type
    }

    response = gxutils.send_rpc(manager, 'get-conditions', request)
    return response


def get_config(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'get-config', request)
    return response


def get_file(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            path_name - str - If name is a directory, display its list, if name 
                is a file, display its contents. The path can be relative to the 
                /storage directory or absolute.

    ----------------------------
    """

    path_name = kwargs.get('path_name', None)

    manager = kwargs.get('manager')

    request = {
        "path-name": path_name
    }

    response = gxutils.send_rpc(manager, 'get-file', request)
    return response


def get_log(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            log_file_name - unknown - The log file to read; must match a 
                currently configured log-file.
            start_time - str - Returns log entries starting from this timestamp. 
                If not provided, consider the oldest available logs.
            end_time - str - Returns log entries ending at this timestamp. If 
                not provided, consider all the logs until the most recent timestamp.
            number_of_entries - str - Describes the amount of log entries that 
                are to be returned.
            pattern_match - str - Allows to provide a regex that filters log 
                entries.

    ----------------------------
    """

    log_file_name = kwargs.get('log_file_name', None)
    start_time = kwargs.get('start_time', None)
    end_time = kwargs.get('end_time', None)
    number_of_entries = kwargs.get('number_of_entries', None)
    pattern_match = kwargs.get('pattern_match', None)

    manager = kwargs.get('manager')

    request = {
        "log-file-name": log_file_name,
        "start-time": start_time,
        "end-time": end_time,
        "number-of-entries": number_of_entries,
        "pattern-match": pattern_match
    }

    response = gxutils.send_rpc(manager, 'get-log', request)
    return response


def get_pm(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            data_type - str - Type of PM data to retrieve.
            number_of_records - int - Maximum number of records that will be 
                retrieved.
            skip_records - int - Allows user to specify a number of records that 
                will be skipped, so that the total data can be fetched in multiple 
                requests. Example: - system has 2300 PM records available - 1st 
                get-pm with (number-of-records = 1000) and (skip-records = 0); 
                result has 0..1000 records - 2nd get-pm with (number-of-records = 
                1000) and (skip-records = 1000); result has 1001..2000 records - 3nd 
                get-pm with (number-of-records = 1000) and (skip-records = 2000); 
                result has 2001..2300 records
            period - str - Time period for PM data.
            start_time - str - If provided, defines the start timestamp that 
                will be considered to filter the PM results. If not provided, the 
                oldest data timestamp will be considered.
            end_time - str - If provided, defines the end timestamp that will be 
                considered to filter the PM results. If not provided, the most 
                recent data timestamp will be considered.
            start_bin - int - If provided, defines the start bin number that 
                will be considered to filter the PM results. If not provided, the 
                smallest bin number (most recent data) will be considered.
            end_bin - int - If provided, defines the end bin number that will be 
                considered to filter the PM results. If not provided, the largest 
                available bin number (oldest data) will be considered.
            filter_list - list - List of:
                filter-id - int - Identifier for each filter, has no specific meaning.
                resource - str - Existing system resource.
                resource-type - str - Type of resource.
                AID - str - Resource Access Identifier (AID). Identifies an instance 
                    within a specific resource type.
                parameter - str - PM parameter identifier (can be a counter or a 
                    gauge).
                direction - str - PM parameter direction.
                location - str - PM parameter location.

    ----------------------------
    """

    data_type = kwargs.get('data_type', None)
    number_of_records = kwargs.get('number_of_records', None)
    skip_records = kwargs.get('skip_records', None)
    period = kwargs.get('period', None)
    start_time = kwargs.get('start_time', None)
    end_time = kwargs.get('end_time', None)
    start_bin = kwargs.get('start_bin', None)
    end_bin = kwargs.get('end_bin', None)
    filter_list = kwargs.get('filter_list', None)

    manager = kwargs.get('manager')

    request = {
        "data-type": data_type,
        "number-of-records": number_of_records,
        "skip-records": skip_records,
        "period": period,
        "start-time": start_time,
        "end-time": end_time,
        "start-bin": start_bin,
        "end-bin": end_bin,
        "filter": filter_list
    }

    response = gxutils.send_rpc(manager, 'get-pm', request)
    return response


def get_schema(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            identifier - str - Identifier for the schema list entry.
            version - str - Version of the schema requested. If this parameter 
                is not present, and more than one version of the schema exists on 
                the server, a 'data-not-unique' error is returned, as described above.
            format - str - The data modeling language of the schema. If this 
                parameter is not present, and more than one formats of the schema 
                exists on the server, a 'data-not-unique' error is returned, as 
                described above.

    ----------------------------
    """

    identifier = kwargs.get('identifier', None)
    version = kwargs.get('version', None)
    format = kwargs.get('format', None)

    manager = kwargs.get('manager')

    request = {
        "identifier": identifier,
        "version": version,
        "format": format
    }

    response = gxutils.send_rpc(manager, 'get-schema', request)
    return response


def get_script(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            list_scripts - str - List all existing scripts.
            script_name - str - Get the content of an existing script. The 
                script name is a relative path to the script directory.

    ----------------------------
    """

    list_scripts = kwargs.get('list_scripts', None)
    script_name = kwargs.get('script_name', None)

    manager = kwargs.get('manager')

    request = {
        "list-scripts": list_scripts,
        "script-name": script_name
    }

    response = gxutils.send_rpc(manager, 'get-script', request)
    return response


def get(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'get', request)
    return response


def import_certificate(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            type - str - Certificate types available for import.
            certificate_name - str - X509v3 local/peer/trusted certificate ID.
            certificate_pem - str - Certificate bytes or certificates bundle in 
                PEM format.
            passphrase - str - To decode encrypted input certificates.
            intermediate_import - bool - Allow to import any intermediate 
                certificates present in a PEM string bundle. If certificate-name is 
                not provided, it will be auto-generated from the topmost certificate 
                issuer CN plus a numeric suffix.

    ----------------------------
    """

    type = kwargs.get('type', None)
    certificate_name = kwargs.get('certificate_name', None)
    certificate_pem = kwargs.get('certificate_pem', None)
    passphrase = kwargs.get('passphrase', None)
    intermediate_import = kwargs.get('intermediate_import', None)

    manager = kwargs.get('manager')

    request = {
        "type": type,
        "certificate-name": certificate_name,
        "certificate-pem": certificate_pem,
        "passphrase": passphrase,
        "intermediate-import": intermediate_import
    }

    response = gxutils.send_rpc(manager, 'import-certificate', request)
    return response


def install_krp(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            krp_name - str - Key replacement package name

    ----------------------------
    """

    krp_name = kwargs.get('krp_name', None)

    manager = kwargs.get('manager')

    request = {
        "krp-name": krp_name
    }

    response = gxutils.send_rpc(manager, 'install-krp', request)
    return response


def kill_session(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            session_id - unknown - Identifier of the session that will be killed.

    ----------------------------
    """

    session_id = kwargs.get('session_id', None)

    manager = kwargs.get('manager')

    request = {
        "session-id": session_id
    }

    response = gxutils.send_rpc(manager, 'kill-session', request)
    return response


def lock(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'lock', request)
    return response


def manual_switchover(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            resource - str - Active controller card to switchover.

    ----------------------------
    """

    resource = kwargs.get('resource', None)

    manager = kwargs.get('manager')

    request = {
        "resource": resource
    }

    response = gxutils.send_rpc(manager, 'manual-switchover', request)
    return response


def no_op(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'no-op', request)
    return response


def password(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            old_password - str - The current password.
            new_password - str - The new password.

    ----------------------------
    """

    old_password = kwargs.get('old_password', None)
    new_password = kwargs.get('new_password', None)

    manager = kwargs.get('manager')

    request = {
        "old-password": old_password,
        "new-password": new_password
    }

    response = gxutils.send_rpc(manager, 'password', request)
    return response


def ping(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            ping_count - int - Stops after sending 'count' ECHO_REQUEST packets.
            ping_timeout - int - Specify the timeout, in seconds, before ping 
                exits.
            ping_pktsize - int - Specifies the number of bytes to be sent. 
                Default is 56, exclusive of headers.
            ping_dest - str - IP address or FQDN of the destination node.
            ping_interface - unknown - Specify source interface name
            ping_vrf - str - VRF to use. If not provided, defaults to MGMT.

    ----------------------------
    """

    ping_count = kwargs.get('ping_count', None)
    ping_timeout = kwargs.get('ping_timeout', None)
    ping_pktsize = kwargs.get('ping_pktsize', None)
    ping_dest = kwargs.get('ping_dest', None)
    ping_interface = kwargs.get('ping_interface', None)
    ping_vrf = kwargs.get('ping_vrf', None)

    manager = kwargs.get('manager')

    request = {
        "ping-count": ping_count,
        "ping-timeout": ping_timeout,
        "ping-pktsize": ping_pktsize,
        "ping-dest": ping_dest,
        "ping-interface": ping_interface,
        "ping-vrf": ping_vrf
    }

    response = gxutils.send_rpc(manager, 'ping', request)
    return response


def prepare_upgrade(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            option - str - Predefined options available for prepare-upgrade
            manifest - unknown - manifest to be prepared for upgrade
            ignore_precheck_failures - bool - Ignore validation failures.
            unattended - bool - Auto activate software after prepare upgrade.
            db_action - str - Specify the expected database operation during 
                activating software image.

    ----------------------------
    """

    option = kwargs.get('option', None)
    manifest = kwargs.get('manifest', None)
    ignore_precheck_failures = kwargs.get('ignore_precheck_failures', None)
    unattended = kwargs.get('unattended', None)
    db_action = kwargs.get('db_action', None)

    manager = kwargs.get('manager')

    request = {
        "option": option,
        "manifest": manifest,
        "ignore-precheck-failures": ignore_precheck_failures,
        "unattended": unattended,
        "db-action": db_action
    }

    response = gxutils.send_rpc(manager, 'prepare-upgrade', request)
    return response


def protection_switch(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            protection_group - str - The target of the switch command.
            operation_type - str - The type of protection switch command
            switch_target - str - The target of the switch command, which is not 
                needed for release and lockout operation.

    ----------------------------
    """

    protection_group = kwargs.get('protection_group', None)
    operation_type = kwargs.get('operation_type', None)
    switch_target = kwargs.get('switch_target', None)

    manager = kwargs.get('manager')

    request = {
        "protection-group": protection_group,
        "operation-type": operation_type,
        "switch-target": switch_target
    }

    response = gxutils.send_rpc(manager, 'protection-switch', request)
    return response


def re_auth(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            ikev2_peer - str - A reference to the IKE peer object (IKE SA).

    ----------------------------
    """

    ikev2_peer = kwargs.get('ikev2_peer', None)

    manager = kwargs.get('manager')

    request = {
        "ikev2-peer": ikev2_peer
    }

    response = gxutils.send_rpc(manager, 're-auth', request)
    return response


def re_key(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            ipsec_security_association - str - Points to IPsec SPD entry object 
                (Child SA).
            ikev2_peer - str - A reference to the IKE peer object (IKE SA).
            secure_entity - str - Points to secure entity object (Child SA).

    ----------------------------
    """

    ipsec_security_association = kwargs.get('ipsec_security_association', None)
    ikev2_peer = kwargs.get('ikev2_peer', None)
    secure_entity = kwargs.get('secure_entity', None)

    manager = kwargs.get('manager')

    request = {
        "ipsec-security-association": ipsec_security_association,
        "ikev2-peer": ikev2_peer,
        "secure-entity": secure_entity
    }

    response = gxutils.send_rpc(manager, 're-key', request)
    return response


def restart(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            resource - str - Resource to restart. If not provided, by default 
                restarts the node controller.
            type - str - Restart type
            sub_component - str - Allows to target a card sub-component to 
                restart.

    ----------------------------
    """

    resource = kwargs.get('resource', None)
    type = kwargs.get('type', None)
    sub_component = kwargs.get('sub_component', None)

    manager = kwargs.get('manager')

    request = {
        "resource": resource,
        "type": type,
        "sub-component": sub_component
    }

    response = gxutils.send_rpc(manager, 'restart', request)
    return response


def run_script(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            script_name - str - Script absolute or relative path from the script 
                directory.
            arguments - str - Optional arguments to the script.

    ----------------------------
    """

    script_name = kwargs.get('script_name', None)
    arguments = kwargs.get('arguments', None)

    manager = kwargs.get('manager')

    request = {
        "script-name": script_name,
        "arguments": arguments
    }

    response = gxutils.send_rpc(manager, 'run-script', request)
    return response


def run_task(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            task_name - unknown - The task name to be executed.

    ----------------------------
    """

    task_name = kwargs.get('task_name', None)

    manager = kwargs.get('manager')

    request = {
        "task-name": task_name
    }

    response = gxutils.send_rpc(manager, 'run-task', request)
    return response


def set_alarm_state(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            state - str - Alarm state.
            acknowledge_text - str - Optional text that will be stored in the 
                alarm.
            all_alarms - str - Acknowledge all currently raised alarms.

    ----------------------------
    """

    state = kwargs.get('state', None)
    acknowledge_text = kwargs.get('acknowledge_text', None)
    all_alarms = kwargs.get('all_alarms', None)

    manager = kwargs.get('manager')

    request = {
        "state": state,
        "acknowledge-text": acknowledge_text,
        "all-alarms": all_alarms
    }

    response = gxutils.send_rpc(manager, 'set-alarm-state', request)
    return response


def set_time(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            new_time - str - Time to set in the system

    ----------------------------
    """

    new_time = kwargs.get('new_time', None)

    manager = kwargs.get('manager')

    request = {
        "new-time": new_time
    }

    response = gxutils.send_rpc(manager, 'set-time', request)
    return response


def simulate(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            trigger - str - The alarm event trigger to simulate.
            holder_AID - str - AID of the equipment holder (slot or port) where 
                the equipment will be simulated.
            type - str - The type of the equipment to be simulated.
            subtype - str - The subtype of the equipment to be simulated.
            alarmed_entity - str - The entity affected by the alarm; if ommitted 
                when clearing alarms, all simulated alarms are cleared.
            alarm_type - str - The alarm type to be simulated; if ommitted when 
                clearing alarms, all simulated alarms are cleared.
            alarm_direction - str - The direction of the simulated alarm. If 
                ommitted, system selects direction automatically.
            alarm_location - str - The location of the simulated alarm. If 
                ommitted, system selects location automatically.

    ----------------------------
    """

    trigger = kwargs.get('trigger', None)
    holder_AID = kwargs.get('holder_AID', None)
    type = kwargs.get('type', None)
    subtype = kwargs.get('subtype', None)
    alarmed_entity = kwargs.get('alarmed_entity', None)
    alarm_type = kwargs.get('alarm_type', None)
    alarm_direction = kwargs.get('alarm_direction', None)
    alarm_location = kwargs.get('alarm_location', None)

    manager = kwargs.get('manager')

    request = {
        "trigger": trigger,
        "holder-AID": holder_AID,
        "type": type,
        "subtype": subtype,
        "alarmed-entity": alarmed_entity,
        "alarm-type": alarm_type,
        "alarm-direction": alarm_direction,
        "alarm-location": alarm_location
    }

    response = gxutils.send_rpc(manager, 'simulate', request)
    return response


def ssh_keygen(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            key_length - str - Strength of the key used for regenerating the 
                private-public key pair
            key_type - str - Type of key to generate
            key_label - str - Label associated with the key. If no value 
                provided, label will be the value of ne-id

    ----------------------------
    """

    key_length = kwargs.get('key_length', None)
    key_type = kwargs.get('key_type', None)
    key_label = kwargs.get('key_label', None)

    manager = kwargs.get('manager')

    request = {
        "key-length": key_length,
        "key-type": key_type,
        "key-label": key_label
    }

    response = gxutils.send_rpc(manager, 'ssh-keygen', request)
    return response


def take_snapshot(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            type - str - Location where the snapshot will be stored.
            db_instance - str - Target db-instance name which will hold the DB 
                snapshot.
            description - str - Optional description for this DB snapshot.
            db_passphrase - str - Passphrase used for encrypting and decrypting 
                DB snapshots. For each command associated with DB snapshots (backup, 
                restore, etc), this db-passphrase will be used, except when it is 
                directly provided in each command. Automatic DB snapshots will not 
                be enabled until this parameter is set.

    ----------------------------
    """

    type = kwargs.get('type', None)
    db_instance = kwargs.get('db_instance', None)
    description = kwargs.get('description', None)
    db_passphrase = kwargs.get('db_passphrase', None)

    manager = kwargs.get('manager')

    request = {
        "type": type,
        "db-instance": db_instance,
        "description": description,
        "db-passphrase": db_passphrase
    }

    response = gxutils.send_rpc(manager, 'take-snapshot', request)
    return response


def traceroute(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            tr_hopcnt - int - Specifies the maximum number of hops (max 
                time-to-live value) traceroute will probe. The default is 10.
            tr_timeout - int - Specify the timeout, in seconds, before trace 
                route exits.
            tr_dest - str - IPv4/v6 address or FQDN of the destination node.
            tr_pktsize - int - Specifies the total size of the probing packet 
                (default 60 bytes for IPv4).
            tr_interface - unknown - Specify source interface name
            tr_vrf - str - VRF to use. If not provided, defaults to MGMT.

    ----------------------------
    """

    tr_hopcnt = kwargs.get('tr_hopcnt', None)
    tr_timeout = kwargs.get('tr_timeout', None)
    tr_dest = kwargs.get('tr_dest', None)
    tr_pktsize = kwargs.get('tr_pktsize', None)
    tr_interface = kwargs.get('tr_interface', None)
    tr_vrf = kwargs.get('tr_vrf', None)

    manager = kwargs.get('manager')

    request = {
        "tr-hopcnt": tr_hopcnt,
        "tr-timeout": tr_timeout,
        "tr-dest": tr_dest,
        "tr-pktsize": tr_pktsize,
        "tr-interface": tr_interface,
        "tr-vrf": tr_vrf
    }

    response = gxutils.send_rpc(manager, 'traceroute', request)
    return response


def unlock(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'unlock', request)
    return response


def upload(handle, **kwargs):
    """
    ----------------------------
        Inputs:
            filetype - str - Predefined filetype available for upload
            source - str - Allows user to provide the source for the file to be 
                uploaded, including directory and/or filename. This is only 
                applicable when file-type is 'file', representing a generic file 
                transfer. Can be a path relative to the default user directory, or 
                an absolute path - as long as user has access to the target file.
            async_ - bool - Uploads asynchronously.
            skip_secure_verification - bool - For HTTPS transfers, skip TLS 
                verification. For SCP/SFTP transfers, skip ssh known host checking. 
                If flag not set, verification is done according with current 
                security-policy.
            debug_entity - str - Targets a specific entity in the system for 
                having its Logs to be collected. Can be a chassis or a card
            password - str - SFTP/SCP/FTP/HTTP/HTTPS password
            start_time - str - Start time from where the logs should be 
                collected. It can be a timestamp or a time interval from the actual 
                time (now). If empty all log history is selected
            db_instance - str - Selected DB instance
            optional_content - str - List of files to be included for debug-log 
                upload.
            log_file_list - unknown - List of log files to be uploaded. If empty 
                all available logs are selected.
            period - str - Time period for PM data.
            db_passphrase - str - Passphrase used for encrypting and decrypting 
                DB snapshots. For each command associated with DB snapshots (backup, 
                restore, etc), this db-passphrase will be used, except when it is 
                directly provided in each command. Automatic DB snapshots will not 
                be enabled until this parameter is set.
            destination - str - Destination of the upload 
                ([sftp|scp|ftp|https|http|file]://[user@]hostname/directorypath/filename)
                
            file_server - unknown - The preconfigured file-server name.
            path - str - Path (directory and filename) to be used in the remote 
                file-server. If not provided, the file-server initial-path is used, 
                with system defined filename. If the path targets a directory (e.g. 
                /path/ ), the filename is dynamically generated. Otherwise, the user 
                defined filename may use some placeholders %t and %m (representing 
                timestamp and ne-name respectively).

    ----------------------------
    """

    filetype = kwargs.get('filetype', None)
    source = kwargs.get('source', None)
    async_ = kwargs.get('async_', None)
    skip_secure_verification = kwargs.get('skip_secure_verification', None)
    debug_entity = kwargs.get('debug_entity', None)
    password = kwargs.get('password', None)
    start_time = kwargs.get('start_time', None)
    db_instance = kwargs.get('db_instance', None)
    optional_content = kwargs.get('optional_content', None)
    log_file_list = kwargs.get('log_file_list', None)
    period = kwargs.get('period', None)
    db_passphrase = kwargs.get('db_passphrase', None)
    destination = kwargs.get('destination', None)
    file_server = kwargs.get('file_server', None)
    path = kwargs.get('path', None)

    manager = kwargs.get('manager')

    request = {
        "filetype": filetype,
        "source": source,
        "async": async_,
        "skip-secure-verification": skip_secure_verification,
        "debug-entity": debug_entity,
        "password": password,
        "start-time": start_time,
        "db-instance": db_instance,
        "optional-content": optional_content,
        "log-file-list": log_file_list,
        "period": period,
        "db-passphrase": db_passphrase,
        "destination": destination,
        "file-server": file_server,
        "path": path
    }

    response = gxutils.send_rpc(manager, 'upload', request)
    return response


def validate(handle, **kwargs):
    """
    ----------------------------
        Inputs:

    ----------------------------
    """


    manager = kwargs.get('manager')

    request = {}

    response = gxutils.send_rpc(manager, 'validate', request)
    return response


