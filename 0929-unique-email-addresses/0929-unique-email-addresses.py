class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def getEmail(email):
            local, domain = email.split('@')
            newLocal = []

            for c in local:
                if c == '+':
                    break
                if c == '.':
                    continue
                newLocal.append(c)
            
            return ''.join(newLocal) + '@' + domain
        
        emailSet = set()
        for email in emails:
            emailSet.add(getEmail(email))
        
        return len(emailSet)