import json
import os
from typing import List

from swagger_client.rest import ApiException
from config import KLAVIYO_CLIENT as client


def get_lists():
    """
    Get all lists
    :return: List of dictionaries containing List Id and List Name
    """
    try:
        return client.ListsSegments.get_lists()
    except ApiException as exception:
        print(f'Unable to get the mailing lists details: {exception.__str__()}')
        raise


def get_list_info(list_id: str):
    """
    Get the information of a given mailing list
    :param list_id: List If
    :return: returns the dict contains the information of the mailing list
    """
    try:
        return client.ListsSegments.get_list_info(list_id)
    except ApiException as exception:
        print(f'Unable to get the mailing list info: {exception.__str__()}')
        raise


def create_list(list_name):
    """
    Method to create a new Mailing List
    :param list_name: List Name
    :return: Dict with list_id
    """
    try:
        return client.ListsSegments.create_list(list_name=list_name)
    except ApiException as exception:
        print(f'Unable to create the list: {json.loads(exception.body)["detail"]}')
        raise


def add_member_to_list(list_id: str, member_list: List):
    """
    Method to add members to an existing list
    :param list_id: List Id
    :param member_list: List of member emails (strings)
    :return: return if not error is occurred
    """
    data_dict = {
        "profiles": []
    }
    for member in member_list:
        data_dict['profiles'].append({
            "email": member
        })

    # Make the request
    try:
        response = client.ListsSegments.add_members(list_id, body=data_dict)
    except ApiException as exception:
        print(f'Unable to add member to the list: {json.loads(exception.body)["detail"]}')
        raise


def get_segment_or_list_member(list_or_segment_id, marker=1):
    """
    Get the list of members of a given list/segment
    :param list_or_segment_id: List of Segment Id
    :param marker: Marker that is returned from previous list
    """
    try:
        response = client.ListsSegments.get_members(list_or_segment_id, marker=marker)
        if response['records']:
            return response['records']
        else:
            return []
    except ApiException as exception:
        print(f'Unable to get list of members for list/segment: {json.loads(exception.body)["detail"]}')
        raise
