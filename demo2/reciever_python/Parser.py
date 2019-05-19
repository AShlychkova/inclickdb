"""
parsing data with templates
parsing data with templates
"""
import datetime


def parse_tagged_data(data, taglist=[]):

    """
    :param data: string form of mectic
    :param Taglist: list of column in table
    :return:
        insert_data - dict of data to insert into table;
        tag_to_add -  tags that are not in taglist;
        tags - tags for insert query
    """

    if isinstance(data) != str:
        data = data.decode("utf-8")

    data = data.split()
    if len(data) != 3:
        return None, None, None

    insert_data = dict()
    insert_data["timestmp"] = int(data[2])
    insert_data["last_volume"] = int(data[1])
    data = data[0].split(";")
    insert_data["path"] = data[0]
    tag_to_add = []
    data = data[1:]
    tags = "timestmp, path, last_volume"
    for tag_value in data:

        tag = tag_value.split("=")[0]
        value = int(tag_value.split("=")[1])

        tags += ", " + tag

        insert_data[tag] = value
        if tag not in taglist:
            tag_to_add.append(tag)

    return insert_data, tag_to_add, tags


def is_match(tmp, data, names, taglist=[]):
    """
    :param tmp: string template
    :param taglist: list of column in table
    :return:
        insert_data - dict of data to insert into table;
        tag_to_add -  tags that are not in taglist;
        tags - tags for insert query
    """
    tmp = tmp.split(".")
    data = data.split()
    data_ = data[0].split(".")
    names = names.split(".")
    insert_data = dict()
    path = ""
    last_volume = ""
    tag_to_add = []
    tags = "timestmp, path, last_volume"

    for i in range(len(tmp)):
        if tmp[i] != "*":
            if data_[i] != tmp[i]:
                return None, None, None
        if names[i] == "measurement":
            path += data_[i] + "."
        elif names[i] == "field":
            last_volume += data_[i]
        elif names[i] != "":
            insert_data[names[i]] = data_[i]
            if names[i] not in taglist:
                tag_to_add.append(names[i])
            tags += ", " + names[i]

    insert_data[last_volume] = data[-1]
    insert_data["path"] = path
    tmsp = str(datetime.datetime.timestamp(datetime.datetime.now())).split(".")
    insert_data["timestmp"] = int(tmsp[0])
    return insert_data, tag_to_add, tags


def parse_tamplate(filename, data, taglist=[]):
    """
        :param filename: string name of file
        :param taglist: list of column in table
        :param data: data to parse
        :return:
            insert_data - dict of data to insert into table;
            tag_to_add -  tags that are not in taglist;
            tags - tags for insert query
        """
    if isinstance(filename) == str:
        file = open(filename, "r")
    else:
        file = filename

    for line in file:
        linesp = line.split()
        insert_data, tag_to_add, tags = is_match(linesp[0], data, linesp[1], taglist)

        if insert_data:
            return insert_data, tag_to_add, tags
    return None, None, None
