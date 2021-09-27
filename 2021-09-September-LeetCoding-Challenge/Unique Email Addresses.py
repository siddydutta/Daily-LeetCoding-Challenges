# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local_name, domain_name = email.split('@')
            if '+' in email:
                local_name = local_name[:local_name.index('+')]
            local_name = local_name.replace('.', "")

            temp_email = local_name + "@" + domain_name
            unique_emails.add(temp_email)

        return len(unique_emails)


def main():
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com",
              "testemail+david@lee.tcode.com"]
    assert Solution().numUniqueEmails(emails) == 2

    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    assert Solution().numUniqueEmails(emails) == 3


if __name__ == '__main__':
    main()
