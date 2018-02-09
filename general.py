import os


def create_data_dir(directory):
    """
    create a directory to save crawled data and crawling range
    :param directory: the name of directory
    :return: none
    """
    if not os.path.exists(directory):
        print('create a new directory: ' + directory)
        os.makedirs(directory)


def create_date_files(directory):
    queue_file = os.path.join(directory, 'queue.txt')
    crawled_file = os.path.join(directory, 'crawled_data.txt')
    if not os.path.isfile(queue_file):
        open(queue_file, 'w').close()
    if not os.path.isfile(crawled_file):
        open(crawled_file, 'w').close()


def save_to_file(path, data, mode='a'):
    with open(path, mode) as f:
        f.write(data + '\n')


def delete_file(path):
    open(path, 'w').close()
