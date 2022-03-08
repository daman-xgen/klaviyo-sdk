from xgen_klaviyo_sdk.services import \
    get_list_info

if __name__ == '__main__':
    # mail_list = create_list('test_list')
    # if mail_list['list_id']:
    #     add_member_to_list(
    #         list_id=mail_list['list_id'],
    #         member_list=[
    #             'damandeep.dhillon@xgen.ai',
    #             'david.simmerman@xgen.ai',
    #             'louis.cha@xgen.ai',
    #             'ken.wang@xgen.ai'
    #         ]
    #     )
    # members = get_segment_or_list_member(list_or_segment_id='UtDtXh')
    list_info = get_list_info(list_id='UtDtXh')
    print('Done')

