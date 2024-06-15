# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from enum import Enum
from typing import Optional, TypeVar, Union

from pydantic import BaseModel

from cidipi.domains import network

CertificateId = TypeVar("CertificateId", bound=Union[float, int])
"""
An internal certificate ID value.
"""


class MixedContentType(str, Enum):
    """
        A description of mixed content (HTTP resources on HTTPS pages), as defined by
    https://www.w3.org/TR/mixed-content/#categories
    """

    blockable = "blockable"
    optionally_blockable = "optionally-blockable"
    none = "none"


class SecurityState(str, Enum):
    """
    The security level of a page or resource.
    """

    unknown = "unknown"
    neutral = "neutral"
    insecure = "insecure"
    secure = "secure"
    info = "info"
    insecure_broken = "insecure-broken"


class CertificateSecurityState(BaseModel):
    """
    Details about the security state of the page certificate.
    """

    protocol: str
    """
    Protocol name (e.g. "TLS 1.2" or "QUIC").
    """
    keyExchange: str
    """
    Key Exchange used by the connection, or the empty string if not applicable.
    """
    keyExchangeGroup: Optional[str]
    """
    (EC)DH group used by the connection, if applicable.
    """
    cipher: str
    """
    Cipher name.
    """
    mac: Optional[str]
    """
    TLS MAC. Note that AEAD ciphers do not have separate MACs.
    """
    certificate: list
    """
    Page certificate.
    """
    subjectName: str
    """
    Certificate subject name.
    """
    issuer: str
    """
    Name of the issuing CA.
    """
    validFrom: network.TimeSinceEpoch
    """
    Certificate valid from date.
    """
    validTo: network.TimeSinceEpoch
    """
    Certificate valid to (expiration) date
    """
    certificateNetworkError: Optional[str]
    """
    The highest priority network error code, if the certificate has an error.
    """
    certificateHasWeakSignature: bool
    """
    True if the certificate uses a weak signature algorithm.
    """
    certificateHasSha1Signature: bool
    """
    True if the certificate has a SHA1 signature in the chain.
    """
    modernSSL: bool
    """
    True if modern SSL
    """
    obsoleteSslProtocol: bool
    """
    True if the connection is using an obsolete SSL protocol.
    """
    obsoleteSslKeyExchange: bool
    """
    True if the connection is using an obsolete SSL key exchange.
    """
    obsoleteSslCipher: bool
    """
    True if the connection is using an obsolete SSL cipher.
    """
    obsoleteSslSignature: bool
    """
    True if the connection is using an obsolete SSL signature.
    """


class SafetyTipStatus(str, Enum):
    badReputation = "badReputation"
    lookalike = "lookalike"


class SafetyTipInfo(BaseModel):
    safetyTipStatus: "SafetyTipStatus"
    """
    Describes whether the page triggers any safety tips or reputation warnings. Default is unknown.
    """
    safeUrl: Optional[str]
    """
    The URL the safety tip suggested ("Did you mean?"). Only filled in for lookalike matches.
    """


class VisibleSecurityState(BaseModel):
    """
    Security state information about the page.
    """

    securityState: "SecurityState"
    """
    The security level of the page.
    """
    certificateSecurityState: Optional["CertificateSecurityState"]
    """
    Security state details about the page certificate.
    """
    safetyTipInfo: Optional["SafetyTipInfo"]
    """
    The type of Safety Tip triggered on the page. Note that this field will be set even if the Safety Tip UI was not actually shown.
    """
    securityStateIssueIds: list
    """
    Array of security state issues ids.
    """


class SecurityStateExplanation(BaseModel):
    """
    An explanation of an factor contributing to the security state.
    """

    securityState: "SecurityState"
    """
    Security state representing the severity of the factor being explained.
    """
    title: str
    """
    Title describing the type of factor.
    """
    summary: str
    """
    Short phrase describing the type of factor.
    """
    description: str
    """
    Full text explanation of the factor.
    """
    mixedContentType: "MixedContentType"
    """
    The type of mixed content described by the explanation.
    """
    certificate: list
    """
    Page certificate.
    """
    recommendations: Optional[list]
    """
    Recommendations to fix any issues.
    """


class InsecureContentStatus(BaseModel):
    """
    Information about insecure content on the page.
    """

    ranMixedContent: bool
    """
    Always false.
    """
    displayedMixedContent: bool
    """
    Always false.
    """
    containedMixedForm: bool
    """
    Always false.
    """
    ranContentWithCertErrors: bool
    """
    Always false.
    """
    displayedContentWithCertErrors: bool
    """
    Always false.
    """
    ranInsecureContentStyle: "SecurityState"
    """
    Always set to unknown.
    """
    displayedInsecureContentStyle: "SecurityState"
    """
    Always set to unknown.
    """


class CertificateErrorAction(str, Enum):
    """
        The action to take when a certificate error occurs. continue will continue processing the
    request and cancel will cancel the request.
    """

    CONTINUE = "continue"
    cancel = "cancel"