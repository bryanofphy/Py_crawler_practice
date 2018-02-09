import spider

CASE_PREFIX = 'YSC'
CASE_START_NUMBER = 1890036637
RANGE = 1
URL = 'https://egov.uscis.gov/casestatus/landing.do'
PROJECT_NAME = 'res'
NUMBER_OF_RANGES = 10


def crawl():
    case_numbers = []
    start_number = CASE_START_NUMBER
    for j in range(NUMBER_OF_RANGES):
        for i in range(start_number, start_number + RANGE):
            case_number = CASE_PREFIX + str(i)
            case_numbers.append(case_number)
        spider1 = spider.Spider(PROJECT_NAME, URL, case_numbers)
        spider1.craw_page()
        spider1.save_results()
        case_numbers = []
        start_number += RANGE


if __name__ == '__main__':
    crawl()
