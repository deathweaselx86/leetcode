
    
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = {}
        # first remove .
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.','')
            fixed_email = '@'.join([local,domain])
            if fixed_email not in unique_emails:
                unique_emails[fixed_email] = 1
        return len(unique_emails)
        # uh so make these things equal