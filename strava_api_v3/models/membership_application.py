# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MembershipApplication(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'success': 'bool',
        'active': 'bool',
        'membership': 'str'
    }

    attribute_map = {
        'success': 'success',
        'active': 'active',
        'membership': 'membership'
    }

    def __init__(self, success=None, active=None, membership=None):  # noqa: E501
        """MembershipApplication - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._active = None
        self._membership = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if active is not None:
            self.active = active
        if membership is not None:
            self.membership = membership

    @property
    def success(self):
        """Gets the success of this MembershipApplication.  # noqa: E501

        Whether the application for membership was successfully submitted  # noqa: E501

        :return: The success of this MembershipApplication.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this MembershipApplication.

        Whether the application for membership was successfully submitted  # noqa: E501

        :param success: The success of this MembershipApplication.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def active(self):
        """Gets the active of this MembershipApplication.  # noqa: E501

        Whether the membership is currently active  # noqa: E501

        :return: The active of this MembershipApplication.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MembershipApplication.

        Whether the membership is currently active  # noqa: E501

        :param active: The active of this MembershipApplication.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def membership(self):
        """Gets the membership of this MembershipApplication.  # noqa: E501

        The membership status of this application  # noqa: E501

        :return: The membership of this MembershipApplication.  # noqa: E501
        :rtype: str
        """
        return self._membership

    @membership.setter
    def membership(self, membership):
        """Sets the membership of this MembershipApplication.

        The membership status of this application  # noqa: E501

        :param membership: The membership of this MembershipApplication.  # noqa: E501
        :type: str
        """
        allowed_values = ["member", "pending"]  # noqa: E501
        if membership not in allowed_values:
            raise ValueError(
                "Invalid value for `membership` ({0}), must be one of {1}"  # noqa: E501
                .format(membership, allowed_values)
            )

        self._membership = membership

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MembershipApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
