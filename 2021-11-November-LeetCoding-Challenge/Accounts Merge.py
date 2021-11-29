# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ''' Graph based DFS solution. '''
        email_index_map = defaultdict(list)
        # Create a graph of email IDs to their account indices
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                email_index_map[email].append(idx)

        def dfs(idx, emails):
            ''' DFS to traverse the accounts. '''
            if visited[idx]:
                return
            visited[idx] = True
            for email in accounts[idx][1:]:
                emails.add(email)
                for next_idx in email_index_map[email]:
                    dfs(next_idx, emails)

        merged = list()
        visited = [False] * len(accounts)
        for idx, account in enumerate(accounts):
            if not visited[idx]:
                name, emails = account[0], set()
                dfs(idx, emails)
                merged.append([name] + sorted(emails))
        return merged


def main():
    accounts = [['John', 'johnsmith@mail.com', 'john_newyork@mail.com'],
                ['John', 'johnsmith@mail.com', 'john00@mail.com'],
                ['Mary', 'mary@mail.com'],
                ['John', 'johnnybravo@mail.com']]
    merged = [['John', 'john00@mail.com', 'john_newyork@mail.com',
               'johnsmith@mail.com'],
              ['Mary', 'mary@mail.com'],
              ['John', 'johnnybravo@mail.com']]
    assert Solution().accountsMerge(accounts) == merged

    accounts = [['Gabe', 'Gabe0@m.co', 'Gabe3@m.co', 'Gabe1@m.co'],
                ['Kevin', 'Kevin3@m.co', 'Kevin5@m.co', 'Kevin0@m.co'],
                ['Ethan', 'Ethan5@m.co', 'Ethan4@m.co', 'Ethan0@m.co'],
                ['Hanzo', 'Hanzo3@m.co', 'Hanzo1@m.co', 'Hanzo0@m.co'],
                ['Fern', 'Fern5@m.co', 'Fern1@m.co', 'Fern0@m.co']]
    merged = [['Gabe', 'Gabe0@m.co', 'Gabe1@m.co', 'Gabe3@m.co'],
              ['Kevin', 'Kevin0@m.co', 'Kevin3@m.co', 'Kevin5@m.co'],
              ['Ethan', 'Ethan0@m.co', 'Ethan4@m.co', 'Ethan5@m.co'],
              ['Hanzo', 'Hanzo0@m.co', 'Hanzo1@m.co', 'Hanzo3@m.co'],
              ['Fern', 'Fern0@m.co', 'Fern1@m.co', 'Fern5@m.co']]
    assert Solution().accountsMerge(accounts) == merged


if __name__ == '__main__':
    main()
