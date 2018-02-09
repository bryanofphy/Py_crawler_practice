import mechanicalsoup
from datetime import datetime
import general


class Spider:

    def __init__(self, projectname, url, case_numbers):
        self.case_numbers = case_numbers
        self.project_name = projectname
        self.queue_file = self.project_name + '/queue.txt'
        self.crawled_file = self.project_name + '/crawled.txt'
        self.crawled = {}
        self.target_url = url
        general.create_data_dir(projectname)
        general.create_date_files(projectname)

    def craw_page(self):
        """
        start to crawl all case numbers, return data containing information of each case number
        :return: crawled data, a dictionary
        """

        for case_num in self.case_numbers:
            cur_res = self.fetch(case_num)
            self.crawled[case_num] = cur_res

    def fetch(self, case_num):
        """
        return the update date and case status
        :param case_num:
        :return: [case_exist, case_status, update_date]
        """
        case_status = ''
        case_exist = False
        print('now checking case number: ' + case_num)
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(self.target_url)
        browser.select_form('form[name="caseStatusForm"]')
        browser['appReceiptNum'] = case_num
        response = browser.submit_selected()
        start_pos = response.text.find('<div class="rows text-center">')
        # if there is a validation error
        if start_pos == -1:
            print('case number is not valid')
            return [str(case_exist), case_status, 'None']
        else:
            case_exist = True
        case_status = response.text[response.text.find('<h1>', start_pos) + 4:response.text.find('</h1>', start_pos)]
        case_status = case_status.replace(' ', '_')
        second_pos = response.text.find(', ', start_pos)+1
        case_update_date = response.text[
                           response.text.find('<p>', start_pos) + 3 + 3:response.text.find(', ', second_pos)]
        try:
            dt_obj = datetime.strptime(case_update_date, '%B %d, %Y')
            print('case is ' + case_status)
            return [str(case_exist), case_status, str(dt_obj.date())]
        except:
            return [str(case_exist), case_status, 'NA']
        #dt_obj = datetime.strptime(case_update_date, '%B %d, %Y')
        #print('case is ' + case_status)
        #return [str(case_exist), case_status, str(dt_obj.date())]

    def save_results(self):
        """
        save the crawled data to the crawled file
        :return: none
        """

        for case_n, case_status in self.crawled.items():
            status_str = ' '.join(case_status)
            case_n = case_n + ' ' + status_str
            general.save_to_file(self.crawled_file, case_n)



