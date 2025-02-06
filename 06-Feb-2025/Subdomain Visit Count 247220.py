# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        ans = []
        for d in cpdomains:
            domain = d.split()
            domains[domain[1]] += int(domain[0])
            subdomain = domain[1].split(".")
            if len(subdomain) > 2:
                domains["".join(subdomain[2:])] += int(domain[0])
            domains[".".join(subdomain[1:])] += int(domain[0])
        for k, v in domains.items():
            ans.append(" ".join([str(v), k]))
        return ans