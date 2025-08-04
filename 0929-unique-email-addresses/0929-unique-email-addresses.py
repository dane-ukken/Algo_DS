class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def getEmail(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            return local + '@' + domain
        
        emailSet = set()
        for email in emails:
            emailSet.add(getEmail(email))
        
        return len(emailSet)