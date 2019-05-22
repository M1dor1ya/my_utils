def reduce_list_mem(dict_obj):
    """
    此函数用于多重字典列表的数据，当列表元素过多时，无法很好的查看数据结构信息
    所以递归删除字典中所有的列表元素，只保留第一个元素，更易查看数据结构信息
    :param dict_obj:传入一个dict
    :return:返回一个经过递归删除列表元素的dict
    """
    for key,value in dict_obj.items():
        if type(value) is list:
            after_list = []
            for i in value[:5]:
                if type(i) is dict:
                    after = reduce_list_mem(i)
                    after_list.append(after)
                else:
                    after_list.append(i)
            dict_obj.update({key:after_list})
        if type(value) is dict:
            after = reduce_list_mem(value)
            dict_obj.update({key:after})
    return dict_obj