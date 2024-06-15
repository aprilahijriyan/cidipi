# AUTO-GENERATED By cidipi/tools/generator.py. DO NOT EDIT.

from typing import *

from pydantic import BaseModel, PrivateAttr

from cidipi.webauthn.types import *


class credentialAdded(BaseModel):
    """
    Triggered when a credential is added to an authenticator.
    """

    __domain__: str = PrivateAttr("WebAuthn")
    authenticatorId: "AuthenticatorId"
    credential: "Credential"


class credentialAsserted(BaseModel):
    """
    Triggered when a credential is used in a webauthn assertion.
    """

    __domain__: str = PrivateAttr("WebAuthn")
    authenticatorId: "AuthenticatorId"
    credential: "Credential"
