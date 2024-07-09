## New Modules

- ioa-dsc-group
- ioa-dsc

## Removed Modules

- iana-if-type
- ietf-alarms
- ietf-interfaces

## New/Changed Elements in Existing Modules

- **ioa-alarm**
  - New Elements:
    - operator-data
- **ioa-amp-raman**
  - New Elements:
    - amplifier-list.amplifier-raman.pump-power.min-target-pump-power
      - Minimum target pump power.
      - Type: str
    - amplifier-list.amplifier-raman.pump-power.max-target-pump-power
      - Maximum target pump power.
      - Type: str
    - amplifier-list.amplifier-raman.number-of-pumps
      - Number of pumps for the requiredequipped card.
      - Type: int
- **ioa-amp**
  - New Elements:
    - amplifier-list.amplifier.partner-amplifier
      - The partner amplifier for PAx/ BAX instalments
      - Type: str
    - amplifier-list.amplifier.amp-control-support
      - Whether 'controlmode' can be configured as 'automaxpw' or not.
      - Type: str
      - Values: auto, manual-only
    - amplifier-list.amplifier.actual-transmission-band
      - Currently assigned transmission band. If amplifier is not at a degree, it will be 4.85 THz by convention.
      - Type: str
      - Values: c-band-4.85THz, c-band-6.1THz
    - amplifier-list.amplifier.interstage-support
      - 'true' if interstage port is supported in this amplifier.
      - Type: bool
- **ioa-capabilities**
  - New Elements:
    - capabilities.system-capabilities.equipment-capabilities.supported-chassis.default-subtype
      - Default subtype Supported by chassis.
      - Type: str
    - capabilities.system-capabilities.equipment-capabilities.supported-chassis.fan-adjustment-on-altitude
      - Whether FAN(s) rotation are automatically adjusting based on the configured altitude.
      - Type: bool
    - capabilities.system-capabilities.equipment-capabilities.supported-chassis.supported-subtype
      - Supported chassis subtypes; may be empty if chassis doesn't support subtypes.
      - Type: str
    - capabilities.system-capabilities.equipment-capabilities.supported-card.grid-mode-support
      - gridmode capabilities.
    Only of relevance for linecard(s).
      - Type: str
      - Values: not-applicable, flexible-c-band-only, general-c-band, general-fixed-c-band
    - capabilities.system-capabilities.equipment-capabilities.supported-card.node-type-compatibility
      - Node Type Compatibility refers to supported NE Nodetype for a sled card.
    Only of relevance for linecard(s) and carriercard(s).
      - Type: str
- **ioa-certificate**
  - New Elements:
    - x509-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - certificates.certificates.trusted-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - certificates.certificates.local-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - certificates.certificates.peer-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
  - Removed Elements:
    - x509-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - certificates.certificates.trusted-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - certificates.certificates.local-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - certificates.certificates.peer-certificate.white-listed
      - If true, peercertificate does not have an associated trustchain, and was explicitly whitelisted at import time.
Otherwise, it has an associated trustchain.
    - certificates.certificates.peer-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
- **ioa-equipment**
  - New Elements:
    - equipment.equipment.equipment-policies.global-power-profile
      - Allows configuration of the power profile used for all instances of a given
card type, if that card supports powerprofiles.
Alternatively, the globalpowerprofile can be disabled, which means each card
instance will have its own power profile individually configurable.
Changing the globalpowerprofile will have impact on both existing card instances,
as well as newly created card instances.
Power profiles are a way to categorize the power estimation for the system.
- **ioa-equipment**
  - New Elements:
    - equipment.equipment.chassis.required-subtype
      - The subtype of the chassis
      - Type: str
    - equipment.equipment.chassis.equipment-discovery-ready
      - Represents the equipment discovery state for the current chassis.
It will remain as 'false' until all equipment was discovered during startup.
Equipment added after startup will not contribute to the update of this state.
      - Type: bool
    - equipment.equipment.card.resources.paired-slot-total-bandwidth
      - Total supported bandwidth for the paired slot connection. This is applicable only for card models that support paired mode.
      - Type: str
    - equipment.equipment.card.resources.paired-slot-available-bandwidth
      - Available bandwidth for the paired slot connection. This is applicable only for card models that support paired mode.
      - Type: str
    - equipment.equipment.card.last-reboot-time
      - Timestamp of the last reboot event of a card.
      - Type: str
- **ioa-facilities**
  - New Elements:
    - facilities.facilities.spectrum
      - OMS specific equalization within interstage access; and monitoring.
    - facilities.facilities.ochm
      - ochm: Optical Channel nonintrusive monitoring.
ECDP within OMSnim.
    - facilities.facilities.dsc
      - Facility describing the dsc. Refer to G.709.1 and G.709.3
    - facilities.facilities.dsc-group
      - Facility describing the dscgroup.
- **ioa-facilities**
  - New Elements:
    - facilities.facilities.ots.osc-compatibility
      - Informs the system about the connected 7100 compatibility required.
      - Type: str
      - Values: osc-g30, osc-7100
    - facilities.facilities.ots.osc-less-support
      - 'true' if OTS port supports OSCless operation.
      - Type: bool
    - facilities.facilities.ots.span-loss-reference
      - Configures spanloss source intended to be used by the system to calculate automatic target powers.
      - Type: str
      - Values: measured, configured
    - facilities.facilities.ots.span-loss-alarm-threshold
      - Configures the threshold for the SPANLOSSHIGH alarm.
      - Type: str
    - facilities.facilities.ots.span-loss-derived-tx
      - Measured span loss transmit.
      - Type: str
    - facilities.facilities.osc.oscc-support
      - OSC Control support.
      - Type: bool
    - facilities.facilities.osc.tx-power-adjustment
      - Adjustment to the automatically calculated Tx power target.
      - Type: str
    - facilities.facilities.oms.wss-less
      - True if there is no WSS component in the Degree.
      - Type: bool
    - facilities.facilities.oms.assigned-degree
      - Display degree number when card is added in modulesdegree.
      - Type: int
    - facilities.facilities.oms.grid-mode-support
      - Which Cband is supported, for the purpose of gridmode configuration.
      - Type: str
      - Values: not-applicable, flexible-c-band-only, general-c-band, general-fixed-c-band
    - facilities.facilities.nmc.och-connection
      - NMC redux  optical channel connection.
      - Type: bool
    - facilities.facilities.optical-carrier.sop-vector
      - The RX SOP (State Of Polarization) Stokes Vector S1 S2 S3, Example: 0.96, 0.12, 0.22.
    Only of relevance for carrier type OTN.
      - Type: str
    - facilities.facilities.otu.tx-mapping-mode
      - The tx mapping mode of client port. The possible values are dependent on the HW and configuration.
      - Type: str
      - Values: GMP, BMP, openZR+, FlexE-4x100G, GFP-F, GFP-F-extOPU2, AMP, iGMP, none
    - facilities.facilities.otu.expected-mapping-mode
      - The expected mapping mode of client port. The possible values are dependent on the HW and configuration.
      - Type: str
      - Values: GMP, BMP, openZR+, FlexE-4x100G, GFP-F, GFP-F-extOPU2, AMP, iGMP, none
    - facilities.facilities.odu.odu-diagnostics.test-signal-monitoring-type
      - The type of test pattern that is monitored.
      - Type: str
      - Values: none, PRBS31Q, PRBS13Q, scrambled-idles, PRBS9, PRBS31, PRBS31_NONINV
    - facilities.facilities.optical-ptp.actual-power-support
      - Port power monitoring support.
      - Type: str
      - Values: not-applicable, power-rx-tx, power-rx, ocm
  - Removed Elements:
    - facilities.facilities.ots-r.pilot-tone-span-loss
      - The calculated spanloss based on Pilot Tone.
- **ioa-ietf**
  - New Elements:
    - chassis-scope-group
- **ioa-mgmt-protocols**
  - New Elements:
    - protocols.protocols.ssh.ssh-authorized-key.key-expiration-date
      - Expiration date for SSH authorized key.
      - Type: str
    - protocols.protocols.ssh.ssh-authorized-key.key-state
      - State is 'disabled' if key is expired, 'enabled' otherwise.
      - Type: str
      - Values: disabled, enabled
    - protocols.protocols.ssh.ssh-authorized-key.alarm-report-control
      - Controls the reporting of alarms for this particular object.
      - Type: str
      - Values: allowed, inhibited
    - protocols.protocols.cli.show-alarm-columns
      - Columns to display in the output of 'show alarm' CLI command.
Possible options are the standard alarm fields, and additionally the following values:
 defaultcolumns: represents the group of columns shown by default.
      - Type: str
    - protocols.protocols.netconf.static-info-in-notifs
      - List of YANG identifiers that are statically included in notifications.
If they are present in objects that are notified.
Applicable for management protocols with support for YANGtype notifications (NETCONF, etc).
For example, if object user[username='tom'] has had the 'timeout' attribute updated,
and the staticinfoinnotifs included the 'userstatus' string,
the associated notification would include not only the 'timeout' parameter,
but also the 'userstatus' (despite the fact that it had not changed).
      - Type: str
- **ioa-ne-function**
  - New Elements:
    - ne-composition.degree.is-foadm
      - True if there is no WSS component at the Degree and PAx assigned to the degree appropriately.
      - Type: bool
    - ne-composition.degree.wss-less
      - True if there is no WSS component in the Degree.
      - Type: bool
    - ne-composition.adg.modules-adg.ocm-monitoring
      - 'true' if monitoring is provided by the Degree, or CDAD structure; 'false' otherwise.
      - Type: bool
- **ioa-network-element**
  - Removed Elements:
    - system.system.fdr
      - Flight Data Recorder(FDR)
    - ne.system.fdr
      - Flight Data Recorder(FDR)
- **ioa-network-element**
  - New Elements:
    - system.system.sw-management.upgrade-status
      - Provides information of the upgrade status for each entity in the system.
    - ne.equipment.equipment-policies.global-power-profile
      - Allows configuration of the power profile used for all instances of a given
card type, if that card supports powerprofiles.
Alternatively, the globalpowerprofile can be disabled, which means each card
instance will have its own power profile individually configurable.
Changing the globalpowerprofile will have impact on both existing card instances,
as well as newly created card instances.
Power profiles are a way to categorize the power estimation for the system.
    - ne.facilities.spectrum
      - OMS specific equalization within interstage access; and monitoring.
    - ne.facilities.ochm
      - ochm: Optical Channel nonintrusive monitoring.
ECDP within OMSnim.
    - ne.facilities.dsc
      - Facility describing the dsc. Refer to G.709.1 and G.709.3
    - ne.facilities.dsc-group
      - Facility describing the dscgroup.
    - ne.system.sw-management.upgrade-status
      - Provides information of the upgrade status for each entity in the system.
- **ioa-network-element**
  - New Elements:
    - system.system.security.security-policies.minimum-password-length
      - Configurable minimum length for user passwords. When a password is changed, the password length will be verified according with this policy.
Note that changing this policy will not have impact on already set passwords, only on newly set passwords.
The default value will depend on whether the policy strictpasswordcheck is enabled or not (min length is 8 if enabled, 1 if disabled),
but the user is able to override this value by editing this policy manually.
Note: this policy can only be enforced when the password is provided in a nonhashed way.
      - Type: int
    - system.system.security.security-policies.password-history-size
      - The number of passwords to store for password reuse checking.
      - Type: int
    - system.system.security.security-policies.ssh-key-aging-interval
      - This policy defines the sshauthorizedkeys aging interval. Setting the value to 0 disables sshauthorizedkeys aging.
This affects the expiration date of all sshauthorizedkeys. Once aging is enabled, the expiration date is calculated
from current time, for previously configured keys, and from configuration time, for newly configured keys.
      - Type: int
    - system.system.security.certificates.trusted-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - system.system.security.certificates.local-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - system.system.security.certificates.peer-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - system.system.security.aaa-server.auth-protocol
      - The list of supported authentication protocols to use; if more than one is selected, system will try one at a time in a besteffort way.
Authentication will be considered unsuccessful if none of the protocols work.
Only of relevance for protocol supported TACACSPLUS.
      - Type: str
    - system.system.syslog.log-server.sensitive-data
      - Whether the local file has logs include sensitive data.
      - Type: str
      - Values: none, both, only
    - system.system.syslog.log-server.alarm-report-control
      - Controls the reporting of alarms for this particular object.
      - Type: str
      - Values: allowed, inhibited
    - system.system.syslog.log-file.sensitive-data
      - Whether the local file has logs include sensitive data.
      - Type: str
      - Values: none, both, only
    - system.system.syslog.niap-compliant-logging
      - Whether the logs are NIAP compliant.
      - Type: bool
    - system.system.protocols.ssh.ssh-authorized-key.key-expiration-date
      - Expiration date for SSH authorized key.
      - Type: str
    - system.system.protocols.ssh.ssh-authorized-key.key-state
      - State is 'disabled' if key is expired, 'enabled' otherwise.
      - Type: str
      - Values: disabled, enabled
    - system.system.protocols.ssh.ssh-authorized-key.alarm-report-control
      - Controls the reporting of alarms for this particular object.
      - Type: str
      - Values: allowed, inhibited
    - system.system.protocols.cli.show-alarm-columns
      - Columns to display in the output of 'show alarm' CLI command.
Possible options are the standard alarm fields, and additionally the following values:
 defaultcolumns: represents the group of columns shown by default.
      - Type: str
    - system.system.protocols.netconf.static-info-in-notifs
      - List of YANG identifiers that are statically included in notifications.
If they are present in objects that are notified.
Applicable for management protocols with support for YANGtype notifications (NETCONF, etc).
For example, if object user[username='tom'] has had the 'timeout' attribute updated,
and the staticinfoinnotifs included the 'userstatus' string,
the associated notification would include not only the 'timeout' parameter,
but also the 'userstatus' (despite the fact that it had not changed).
      - Type: str
    - system.system.clock.uptime-seconds
      - Indicates how long the system has been running, in seconds.
      - Type: int
    - ne-functions.ne-function.amplifier.partner-amplifier
      - The partner amplifier for PAx/ BAX instalments
      - Type: str
    - ne-functions.ne-function.amplifier.amp-control-support
      - Whether 'controlmode' can be configured as 'automaxpw' or not.
      - Type: str
      - Values: auto, manual-only
    - ne-functions.ne-function.amplifier.actual-transmission-band
      - Currently assigned transmission band. If amplifier is not at a degree, it will be 4.85 THz by convention.
      - Type: str
      - Values: c-band-4.85THz, c-band-6.1THz
    - ne-functions.ne-function.amplifier.interstage-support
      - 'true' if interstage port is supported in this amplifier.
      - Type: bool
    - ne-functions.ne-function.amplifier-raman.pump-power.min-target-pump-power
      - Minimum target pump power.
      - Type: str
    - ne-functions.ne-function.amplifier-raman.pump-power.max-target-pump-power
      - Maximum target pump power.
      - Type: str
    - ne-functions.ne-function.amplifier-raman.number-of-pumps
      - Number of pumps for the requiredequipped card.
      - Type: int
    - ne-functions.ne-function.degree.is-foadm
      - True if there is no WSS component at the Degree and PAx assigned to the degree appropriately.
      - Type: bool
    - ne-functions.ne-function.degree.wss-less
      - True if there is no WSS component in the Degree.
      - Type: bool
    - ne-functions.ne-function.adg.modules-adg.ocm-monitoring
      - 'true' if monitoring is provided by the Degree, or CDAD structure; 'false' otherwise.
      - Type: bool
    - ne.equipment.chassis.required-subtype
      - The subtype of the chassis
      - Type: str
    - ne.equipment.chassis.equipment-discovery-ready
      - Represents the equipment discovery state for the current chassis.
It will remain as 'false' until all equipment was discovered during startup.
Equipment added after startup will not contribute to the update of this state.
      - Type: bool
    - ne.equipment.card.resources.paired-slot-total-bandwidth
      - Total supported bandwidth for the paired slot connection. This is applicable only for card models that support paired mode.
      - Type: str
    - ne.equipment.card.resources.paired-slot-available-bandwidth
      - Available bandwidth for the paired slot connection. This is applicable only for card models that support paired mode.
      - Type: str
    - ne.equipment.card.last-reboot-time
      - Timestamp of the last reboot event of a card.
      - Type: str
    - ne.facilities.ots.osc-compatibility
      - Informs the system about the connected 7100 compatibility required.
      - Type: str
      - Values: osc-g30, osc-7100
    - ne.facilities.ots.osc-less-support
      - 'true' if OTS port supports OSCless operation.
      - Type: bool
    - ne.facilities.ots.span-loss-reference
      - Configures spanloss source intended to be used by the system to calculate automatic target powers.
      - Type: str
      - Values: measured, configured
    - ne.facilities.ots.span-loss-alarm-threshold
      - Configures the threshold for the SPANLOSSHIGH alarm.
      - Type: str
    - ne.facilities.ots.span-loss-derived-tx
      - Measured span loss transmit.
      - Type: str
    - ne.facilities.osc.oscc-support
      - OSC Control support.
      - Type: bool
    - ne.facilities.osc.tx-power-adjustment
      - Adjustment to the automatically calculated Tx power target.
      - Type: str
    - ne.facilities.oms.wss-less
      - True if there is no WSS component in the Degree.
      - Type: bool
    - ne.facilities.oms.assigned-degree
      - Display degree number when card is added in modulesdegree.
      - Type: int
    - ne.facilities.oms.grid-mode-support
      - Which Cband is supported, for the purpose of gridmode configuration.
      - Type: str
      - Values: not-applicable, flexible-c-band-only, general-c-band, general-fixed-c-band
    - ne.facilities.nmc.och-connection
      - NMC redux  optical channel connection.
      - Type: bool
    - ne.facilities.optical-carrier.sop-vector
      - The RX SOP (State Of Polarization) Stokes Vector S1 S2 S3, Example: 0.96, 0.12, 0.22.
    Only of relevance for carrier type OTN.
      - Type: str
    - ne.facilities.otu.tx-mapping-mode
      - The tx mapping mode of client port. The possible values are dependent on the HW and configuration.
      - Type: str
      - Values: GMP, BMP, openZR+, FlexE-4x100G, GFP-F, GFP-F-extOPU2, AMP, iGMP, none
    - ne.facilities.otu.expected-mapping-mode
      - The expected mapping mode of client port. The possible values are dependent on the HW and configuration.
      - Type: str
      - Values: GMP, BMP, openZR+, FlexE-4x100G, GFP-F, GFP-F-extOPU2, AMP, iGMP, none
    - ne.facilities.odu.odu-diagnostics.test-signal-monitoring-type
      - The type of test pattern that is monitored.
      - Type: str
      - Values: none, PRBS31Q, PRBS13Q, scrambled-idles, PRBS9, PRBS31, PRBS31_NONINV
    - ne.facilities.optical-ptp.actual-power-support
      - Port power monitoring support.
      - Type: str
      - Values: not-applicable, power-rx-tx, power-rx, ocm
    - ne.services.oxcon.monitored
      - Monitoring/ notmonitored indication; does not change during oxcon lifetime.
      - Type: bool
    - ne.services.oxcon.circuit-id
      - Path/ service name of optical crossconnection.
      - Type: str
    - ne.system.security.security-policies.minimum-password-length
      - Configurable minimum length for user passwords. When a password is changed, the password length will be verified according with this policy.
Note that changing this policy will not have impact on already set passwords, only on newly set passwords.
The default value will depend on whether the policy strictpasswordcheck is enabled or not (min length is 8 if enabled, 1 if disabled),
but the user is able to override this value by editing this policy manually.
Note: this policy can only be enforced when the password is provided in a nonhashed way.
      - Type: int
    - ne.system.security.security-policies.password-history-size
      - The number of passwords to store for password reuse checking.
      - Type: int
    - ne.system.security.security-policies.ssh-key-aging-interval
      - This policy defines the sshauthorizedkeys aging interval. Setting the value to 0 disables sshauthorizedkeys aging.
This affects the expiration date of all sshauthorizedkeys. Once aging is enabled, the expiration date is calculated
from current time, for previously configured keys, and from configuration time, for newly configured keys.
      - Type: int
    - ne.system.security.certificates.trusted-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - ne.system.security.certificates.local-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - ne.system.security.certificates.peer-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - ne.system.security.aaa-server.auth-protocol
      - The list of supported authentication protocols to use; if more than one is selected, system will try one at a time in a besteffort way.
Authentication will be considered unsuccessful if none of the protocols work.
Only of relevance for protocol supported TACACSPLUS.
      - Type: str
    - ne.system.syslog.log-server.sensitive-data
      - Whether the local file has logs include sensitive data.
      - Type: str
      - Values: none, both, only
    - ne.system.syslog.log-server.alarm-report-control
      - Controls the reporting of alarms for this particular object.
      - Type: str
      - Values: allowed, inhibited
    - ne.system.syslog.log-file.sensitive-data
      - Whether the local file has logs include sensitive data.
      - Type: str
      - Values: none, both, only
    - ne.system.syslog.niap-compliant-logging
      - Whether the logs are NIAP compliant.
      - Type: bool
    - ne.system.protocols.ssh.ssh-authorized-key.key-expiration-date
      - Expiration date for SSH authorized key.
      - Type: str
    - ne.system.protocols.ssh.ssh-authorized-key.key-state
      - State is 'disabled' if key is expired, 'enabled' otherwise.
      - Type: str
      - Values: disabled, enabled
    - ne.system.protocols.ssh.ssh-authorized-key.alarm-report-control
      - Controls the reporting of alarms for this particular object.
      - Type: str
      - Values: allowed, inhibited
    - ne.system.protocols.cli.show-alarm-columns
      - Columns to display in the output of 'show alarm' CLI command.
Possible options are the standard alarm fields, and additionally the following values:
 defaultcolumns: represents the group of columns shown by default.
      - Type: str
    - ne.system.protocols.netconf.static-info-in-notifs
      - List of YANG identifiers that are statically included in notifications.
If they are present in objects that are notified.
Applicable for management protocols with support for YANGtype notifications (NETCONF, etc).
For example, if object user[username='tom'] has had the 'timeout' attribute updated,
and the staticinfoinnotifs included the 'userstatus' string,
the associated notification would include not only the 'timeout' parameter,
but also the 'userstatus' (despite the fact that it had not changed).
      - Type: str
    - ne.system.clock.uptime-seconds
      - Indicates how long the system has been running, in seconds.
      - Type: int
    - ne.ne-function.amplifier.partner-amplifier
      - The partner amplifier for PAx/ BAX instalments
      - Type: str
    - ne.ne-function.amplifier.amp-control-support
      - Whether 'controlmode' can be configured as 'automaxpw' or not.
      - Type: str
      - Values: auto, manual-only
    - ne.ne-function.amplifier.actual-transmission-band
      - Currently assigned transmission band. If amplifier is not at a degree, it will be 4.85 THz by convention.
      - Type: str
      - Values: c-band-4.85THz, c-band-6.1THz
    - ne.ne-function.amplifier.interstage-support
      - 'true' if interstage port is supported in this amplifier.
      - Type: bool
    - ne.ne-function.amplifier-raman.pump-power.min-target-pump-power
      - Minimum target pump power.
      - Type: str
    - ne.ne-function.amplifier-raman.pump-power.max-target-pump-power
      - Maximum target pump power.
      - Type: str
    - ne.ne-function.amplifier-raman.number-of-pumps
      - Number of pumps for the requiredequipped card.
      - Type: int
    - ne.ne-function.degree.is-foadm
      - True if there is no WSS component at the Degree and PAx assigned to the degree appropriately.
      - Type: bool
    - ne.ne-function.degree.wss-less
      - True if there is no WSS component in the Degree.
      - Type: bool
    - ne.ne-function.adg.modules-adg.ocm-monitoring
      - 'true' if monitoring is provided by the Degree, or CDAD structure; 'false' otherwise.
      - Type: bool
    - ne.system-capabilities.equipment-capabilities.supported-chassis.default-subtype
      - Default subtype Supported by chassis.
      - Type: str
    - ne.system-capabilities.equipment-capabilities.supported-chassis.fan-adjustment-on-altitude
      - Whether FAN(s) rotation are automatically adjusting based on the configured altitude.
      - Type: bool
    - ne.system-capabilities.equipment-capabilities.supported-chassis.supported-subtype
      - Supported chassis subtypes; may be empty if chassis doesn't support subtypes.
      - Type: str
    - ne.system-capabilities.equipment-capabilities.supported-card.grid-mode-support
      - gridmode capabilities.
    Only of relevance for linecard(s).
      - Type: str
      - Values: not-applicable, flexible-c-band-only, general-c-band, general-fixed-c-band
    - ne.system-capabilities.equipment-capabilities.supported-card.node-type-compatibility
      - Node Type Compatibility refers to supported NE Nodetype for a sled card.
    Only of relevance for linecard(s) and carriercard(s).
      - Type: str
  - Removed Elements:
    - system.system.security.certificates.trusted-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - system.system.security.certificates.local-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - system.system.security.certificates.peer-certificate.white-listed
      - If true, peercertificate does not have an associated trustchain, and was explicitly whitelisted at import time.
Otherwise, it has an associated trustchain.
    - system.system.security.certificates.peer-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - ne.facilities.ots-r.pilot-tone-span-loss
      - The calculated spanloss based on Pilot Tone.
    - ne.system.security.certificates.trusted-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - ne.system.security.certificates.local-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - ne.system.security.certificates.peer-certificate.white-listed
      - If true, peercertificate does not have an associated trustchain, and was explicitly whitelisted at import time.
Otherwise, it has an associated trustchain.
    - ne.system.security.certificates.peer-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
- **ioa-nmc**
  - New Elements:
    - nmc.nmc.och-connection
      - NMC redux  optical channel connection.
      - Type: bool
- **ioa-odu**
  - Removed Elements:
    - odu-diagnostics
- **ioa-odu**
  - New Elements:
    - odu.odu.odu-diagnostics.test-signal-monitoring-type
      - The type of test pattern that is monitored.
      - Type: str
      - Values: none, PRBS31Q, PRBS13Q, scrambled-idles, PRBS9, PRBS31, PRBS31_NONINV
- **ioa-oms**
  - New Elements:
    - oms-nim
    - dge-equalization
- **ioa-oms**
  - New Elements:
    - oms.oms.wss-less
      - True if there is no WSS component in the Degree.
      - Type: bool
    - oms.oms.assigned-degree
      - Display degree number when card is added in modulesdegree.
      - Type: int
    - oms.oms.grid-mode-support
      - Which Cband is supported, for the purpose of gridmode configuration.
      - Type: str
      - Values: not-applicable, flexible-c-band-only, general-c-band, general-fixed-c-band
- **ioa-optical-carrier**
  - New Elements:
    - carrier.optical-carrier.sop-vector
      - The RX SOP (State Of Polarization) Stokes Vector S1 S2 S3, Example: 0.96, 0.12, 0.22.
    Only of relevance for carrier type OTN.
      - Type: str
  - Removed Elements:
    - client-specific-attrs.loopback
      - Loopback mode.Useful to debug on the fiber connection.
- **ioa-optical-common**
  - New Elements:
    - optical-card-parameters.resources.paired-slot-total-bandwidth
      - Total supported bandwidth for the paired slot connection. This is applicable only for card models that support paired mode.
      - Type: str
    - optical-card-parameters.resources.paired-slot-available-bandwidth
      - Available bandwidth for the paired slot connection. This is applicable only for card models that support paired mode.
      - Type: str
- **ioa-optical-ptp**
  - New Elements:
    - optical-ptp.optical-ptp.actual-power-support
      - Port power monitoring support.
      - Type: str
      - Values: not-applicable, power-rx-tx, power-rx, ocm
- **ioa-osc**
  - New Elements:
    - osc.osc.oscc-support
      - OSC Control support.
      - Type: bool
    - osc.osc.tx-power-adjustment
      - Adjustment to the automatically calculated Tx power target.
      - Type: str
- **ioa-ots-r**
  - Removed Elements:
    - ots-r.ots-r.pilot-tone-span-loss
      - The calculated spanloss based on Pilot Tone.
- **ioa-ots**
  - New Elements:
    - ots.ots.osc-compatibility
      - Informs the system about the connected 7100 compatibility required.
      - Type: str
      - Values: osc-g30, osc-7100
    - ots.ots.osc-less-support
      - 'true' if OTS port supports OSCless operation.
      - Type: bool
    - ots.ots.span-loss-reference
      - Configures spanloss source intended to be used by the system to calculate automatic target powers.
      - Type: str
      - Values: measured, configured
    - ots.ots.span-loss-alarm-threshold
      - Configures the threshold for the SPANLOSSHIGH alarm.
      - Type: str
    - ots.ots.span-loss-derived-tx
      - Measured span loss transmit.
      - Type: str
- **ioa-otu**
  - New Elements:
    - otu.otu.tx-mapping-mode
      - The tx mapping mode of client port. The possible values are dependent on the HW and configuration.
      - Type: str
      - Values: GMP, BMP, openZR+, FlexE-4x100G, GFP-F, GFP-F-extOPU2, AMP, iGMP, none
    - otu.otu.expected-mapping-mode
      - The expected mapping mode of client port. The possible values are dependent on the HW and configuration.
      - Type: str
      - Values: GMP, BMP, openZR+, FlexE-4x100G, GFP-F, GFP-F-extOPU2, AMP, iGMP, none
- **ioa-pm**
  - New Elements:
    - chassis-scope-grouping
- **ioa-pm**
  - New Elements:
    - pm.pm-control.pm-resource.real-time-data-last-reset
      - Date and time of the last real time data reset for this resource. If the data was never reset, this is the date and time of this resource's creation.
      - Type: str
- **ioa-rpc**
  - New Elements:
    - bert-input-parameters
    - bert-result-parameters
- **ioa-rpc**
  - New Elements:
    - db-action.clear-type
      - Defines the type of 'clear database' that the system must do.
      - Type: str
      - Values: full, keep-networking
- **ioa-security**
  - New Elements:
    - security.security.security-policies.minimum-password-length
      - Configurable minimum length for user passwords. When a password is changed, the password length will be verified according with this policy.
Note that changing this policy will not have impact on already set passwords, only on newly set passwords.
The default value will depend on whether the policy strictpasswordcheck is enabled or not (min length is 8 if enabled, 1 if disabled),
but the user is able to override this value by editing this policy manually.
Note: this policy can only be enforced when the password is provided in a nonhashed way.
      - Type: int
    - security.security.security-policies.password-history-size
      - The number of passwords to store for password reuse checking.
      - Type: int
    - security.security.security-policies.ssh-key-aging-interval
      - This policy defines the sshauthorizedkeys aging interval. Setting the value to 0 disables sshauthorizedkeys aging.
This affects the expiration date of all sshauthorizedkeys. Once aging is enabled, the expiration date is calculated
from current time, for previously configured keys, and from configuration time, for newly configured keys.
      - Type: int
    - security.security.certificates.trusted-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - security.security.certificates.local-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - security.security.certificates.peer-certificate.revocation-mode
      - Controls how the revocation status of the certificate is determined.
      - Type: str
      - Values: auto, force-revoked, force-unrevoked
    - security.security.aaa-server.auth-protocol
      - The list of supported authentication protocols to use; if more than one is selected, system will try one at a time in a besteffort way.
Authentication will be considered unsuccessful if none of the protocols work.
Only of relevance for protocol supported TACACSPLUS.
      - Type: str
  - Removed Elements:
    - security.security.certificates.trusted-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - security.security.certificates.local-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
    - security.security.certificates.peer-certificate.white-listed
      - If true, peercertificate does not have an associated trustchain, and was explicitly whitelisted at import time.
Otherwise, it has an associated trustchain.
    - security.security.certificates.peer-certificate.force-revoked
      - If true, the certificate is forced to the 'revoked' status.
- **ioa-services**
  - New Elements:
    - services.services.oxcon.monitored
      - Monitoring/ notmonitored indication; does not change during oxcon lifetime.
      - Type: bool
    - services.services.oxcon.circuit-id
      - Path/ service name of optical crossconnection.
      - Type: str
- **ioa-sw-management**
  - New Elements:
    - upgrade-status
- **ioa-sw-management**
  - New Elements:
    - sw-management.sw-management.upgrade-status
      - Provides information of the upgrade status for each entity in the system.
- **ioa-syslog**
  - New Elements:
    - syslog.syslog.log-server.sensitive-data
      - Whether the local file has logs include sensitive data.
      - Type: str
      - Values: none, both, only
    - syslog.syslog.log-server.alarm-report-control
      - Controls the reporting of alarms for this particular object.
      - Type: str
      - Values: allowed, inhibited
    - syslog.syslog.log-file.sensitive-data
      - Whether the local file has logs include sensitive data.
      - Type: str
      - Values: none, both, only
    - syslog.syslog.niap-compliant-logging
      - Whether the logs are NIAP compliant.
      - Type: bool
- **ioa-time**
  - New Elements:
    - clock.clock.uptime-seconds
      - Indicates how long the system has been running, in seconds.
      - Type: int
- **ioa-transfer**
  - Removed Elements:
    - fdr
