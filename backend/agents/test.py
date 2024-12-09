# import re
# import json

# # The input data (your output as a string)
# data = '''
# ns about these Terms or the Service, please contact us at: Skyline Technologies Pty Ltd123 Digital Way, Level 5Sydney, NSW, AustraliaEmail: support@skyline.comPhone: +61 2 8000 1234 Policies CREDIT CARD TERMS AND CONDITIONS Effective Date : [Date] These Terms and Conditions govern your use of the Credit Card issued by [Bank... © 2023 by My Site. All Rights Reserved"  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# ```json
# {
#   "Terms and Conditions Summary": {
#     "Introduction": {
#       "Effective Date": "December 1, 2024",
#       "Last Updated": "November 29, 2024",
#       "Provider": "Skyline Technologies Pty Ltd",
#       "Agreement": "By using the Service, you agree to these Terms."
#     },
#     "Eligibility": {
#       "Age Requirement": "Must be at least 18 years old.",
#       "Account Creation": "Accurate and current information is required."
#     },
#     "User Responsibilities": {
#       "Account Security": "Maintain confidentiality of account credentials.",
#       "Lawful Use": "Use the Service only for lawful purposes.",
#       "Prohibited Activities": [
#         "Harm or disrupt the Service.",
#         "Upload harmful software.",
#         "Harass or threaten others.",
#         "Gain unauthorized access."
#       ]
#     },
#     "User Content": {
#       "Ownership": "Users retain ownership of their content.",
#       "License": "Users grant Skyline a non-exclusive license to use their content."
#     },
#     "Intellectual Property": {
#       "Skyline Content": "All content provided by Skyline is protected by intellectual property laws."
#     },
#     "Privacy Policy": {
#       "Data Collection": "Personal information is collected for service delivery.",
#       "Data Protection": "Industry-standard encryption is used."
#     },
#     "Subscription and Payments": {
#       "Subscription Plans": {
#         "Basic Plan": "$10/month for 10GB storage.",
#         "Premium Plan": "$30/month for 100GB storage.",
#         "Enterprise Plan": "Custom pricing."
#       },
#       "Payment Methods": [
#         "Credit/Debit Card",
#         "PayPal",
#         "Bank Transfer (Enterprise Plan only)"
#       ],
#       "Refund Policy": "Payments are non-refundable unless stated otherwise."
#     },
#     "Termination": {
#       "Account Termination": "Users can terminate their account at any time.",
#       "Data Retention": "Data retained for 30 days post-termination."
#     },
#     "Limitation of Liability": {
#       "Liability Cap": "Total liability is limited to the amount paid in the last three months."
#     },
#     "Governing Law": {
#       "Jurisdiction": "Laws of New South Wales, Australia."
#     },
#     "Modifications": {
#       "Changes to Terms": "Terms may be modified at any time with notice."
#     },
#     "Contact Information": {
#       "Address": "Skyline Technologies Pty Ltd, 123 Digital Way, Level 5, Sydney, NSW, Australia",
#       "Email": "support@skyline.com",
#       "Phone": "+61 2 8000 1234"
#     }
#   }
# }
# ```INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# Now that I have summarized the key points of the terms and conditions, I need to analyze the risks associated with these terms.  
# Action: Analyze Risks  
# Action Input: (the summarized terms)  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# To proceed with the analysis, I would need the summarized terms and conditions text that you mentioned. Please provide that content so I can identify the risks and categorize the text accordingly.I need to provide the summarized terms and conditions text to analyze the risks.  
# Action: Analyze Risks  
# Action Input: ```json
# {
#   "Terms and Conditions Summary": {
#     "Introduction": {
#       "Effective Date": "December 1, 2024",
#       "Last Updated": "November 29, 2024",
#       "Provider": "Skyline Technologies Pty Ltd",
#       "Agreement": "By using the Service, you agree to these Terms."
#     },
#     "Eligibility": {
#       "Age Requirement": "Must be at least 18 years old.",
#       "Account Creation": "Accurate and current information is required."
#     },
#     "User Responsibilities": {
#       "Account Security": "Maintain confidentiality of account credentials.",
#       "Lawful Use": "Use the Service only for lawful purposes.",
#       "Prohibited Activities": [
#         "Harm or disrupt the Service.",
#         "Upload harmful software.",
#         "Harass or threaten others.",
#         "Gain unauthorized access."
#       ]
#     },
#     "User Content": {
#       "Ownership": "Users retain ownership of their content.",
#       "License": "Users grant Skyline a non-exclusive license to use their content."
#     },
#     "Intellectual Property": {
#       "Skyline Content": "All content provided by Skyline is protected by intellectual property laws."
#     },
#     "Privacy Policy": {
#       "Data Collection": "Personal information is collected for service delivery.",
#       "Data Protection": "Industry-standard encryption is used."
#     },
#     "Subscription and Payments": {
#       "Subscription Plans": {
#         "Basic Plan": "$10/month for 10GB storage.",
#         "Premium Plan": "$30/month for 100GB storage.",
#         "Enterprise Plan": "Custom pricing."
#       },
#       "Payment Methods": [
#         "Credit/Debit Card",
#         "PayPal",
#         "Bank Transfer (Enterprise Plan only)"
#       ],
#       "Refund Policy": "Payments are non-refundable unless stated otherwise."
#     },
#     "Termination": {
#       "Account Termination": "Users can terminate their account at any time.",
#       "Data Retention": "Data retained for 30 days post-termination."
#     },
#     "Limitation of Liability": {
#       "Liability Cap": "Total liability is limited to the amount paid in the last three months."
#     },
#     "Governing Law": {
#       "Jurisdiction": "Laws of New South Wales, Australia."
#     },
#     "Modifications": {
#       "Changes to Terms": "Terms may be modified at any time with notice."
#     },
#     "Contact Information": {
#       "Address": "Skyline Technologies Pty Ltd, 123 Digital Way, Level 5, Sydney, NSW, Australia",
#       "Email": "support@skyline.com",
#       "Phone": "+61 2 8000 1234"
#     }
#   }
# }
# ```  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# ```json
# {
#   "Risks": {
#     "Risk 1": {
#       "Description": "The limitation of liability clause caps the provider's liability to the amount paid in the last three months, which may not cover significant damages incurred by users.",
#       "Category": "Liability"
#     },
#     "Risk 2": {
#       "Description": "The terms allow for modifications at any time with notice, which could lead to unexpected changes that may adversely affect users without their consent.",
#       "Category": "Terms Modification"
#     },
#     "Risk 3": {
#       "Description": "The non-refundable payment policy may pose a risk for users who are dissatisfied with the service or who experience issues shortly after payment.",
#       "Category": "Financial"
#     }
#   }
# }
# ```INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# I have identified the risks associated with the terms and conditions. Now, I need to generate actionable recommendations based on these identified risks.  
# Action: Generate Recommendations  
# Action Input: ```json
# {
#   "Risks": {
#     "Risk 1": {
#       "Description": "The limitation of liability clause caps the provider's liability to the amount paid in the last three months, which may not cover significant damages incurred by users.",
#       "Category": "Liability"
#     },
#     "Risk 2": {
#       "Description": "The terms allow for modifications at any time with notice, which could lead to unexpected changes that may adversely affect users without their consent.",
#       "Category": "Terms Modification"
#     },
#     "Risk 3": {
#       "Description": "The non-refundable payment policy may pose a risk for users who are dissatisfied with the service or who experience issues shortly after payment.",
#       "Category": "Financial"
#     }
#   }
# }
# ```  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# ```json
# {
#   "Recommendations": {
#     "Understand Liability Limits": "Before engaging with the service, carefully review the limitation of liability clause. Consider setting aside a contingency fund to cover potential damages that exceed the capped amount, ensuring you are financially prepared for any unforeseen issues.",
#     "Stay Informed on Terms Changes": "Regularly check for updates to the service terms and conditions. Consider subscribing to notifications or alerts from the provider to stay informed about any modifications that could impact your usage or rights.",
#     "Consider Payment Protection Options": "Explore payment protection options such as credit card chargebacks or third-party payment services that offer buyer protection. This can provide a safety net in case you are dissatisfied with the service or encounter issues shortly after payment."
#   }
# }
# ```INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# I now know the final answer.  
# Final Answer: The terms and conditions from the provided URL outline the rules and responsibilities for using the Skyline Cloud Platform, including user eligibility, account security, ownership of user content, payment details, and limitations of liability. Key risks identified include limited liability for damages, potential for unexpected changes to terms, and a non-refundable payment policy. Recommendations for users include understanding liability limits, staying informed about changes to terms, and considering payment protection options.

# '''

# # Define a function to extract JSON objects
# def extract_json(data):
#     # Regular expression to find all JSON objects enclosed in ```json
#     json_objects = re.findall(r'```json(.*?)```', data, re.DOTALL)
    
#     # Parse the found JSON objects
#     parsed_json_objects = []
#     for json_obj in json_objects:
#         try:
#             parsed_json = json.loads(json_obj.strip())
#             parsed_json_objects.append(parsed_json)
#         except json.JSONDecodeError:
#             continue
    
#     return parsed_json_objects

# # Extract and print JSON objects
# json_objects = extract_json(data)

# # for obj in json_objects:
# #     print(json.dumps(obj, indent=2))


# if __name__ == "__main__":
#     for obj in json_objects:
#         print(json.dumps(obj, indent=4))
#     # print(json_objects)




# import re
# import json

# # The input data (your output as a string)
# data = '''
# ns about these Terms or the Service, please contact us at: Skyline Technologies Pty Ltd123 Digital Way, Level 5Sydney, NSW, AustraliaEmail: support@skyline.comPhone: +61 2 8000 1234 Policies CREDIT CARD TERMS AND CONDITIONS Effective Date : [Date] These Terms and Conditions govern your use of the Credit Card issued by [Bank... © 2023 by My Site. All Rights Reserved"  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# ```json
# {
#   "Terms and Conditions Summary": {
#     "Introduction": {
#       "Effective Date": "December 1, 2024",
#       "Last Updated": "November 29, 2024",
#       "Provider": "Skyline Technologies Pty Ltd",
#       "Agreement": "By using the Service, you agree to these Terms."
#     },
#     "Eligibility": {
#       "Age Requirement": "Must be at least 18 years old.",
#       "Account Creation": "Accurate and current information is required."
#     },
#     "User Responsibilities": {
#       "Account Security": "Maintain confidentiality of account credentials.",
#       "Lawful Use": "Use the Service only for lawful purposes.",
#       "Prohibited Activities": [
#         "Harm or disrupt the Service.",
#         "Upload harmful software.",
#         "Harass or threaten others.",
#         "Gain unauthorized access."
#       ]
#     },
#     "User Content": {
#       "Ownership": "Users retain ownership of their content.",
#       "License": "Users grant Skyline a non-exclusive license to use their content."
#     },
#     "Intellectual Property": {
#       "Skyline Content": "All content provided by Skyline is protected by intellectual property laws."
#     },
#     "Privacy Policy": {
#       "Data Collection": "Personal information is collected for service delivery.",
#       "Data Protection": "Industry-standard encryption is used."
#     },
#     "Subscription and Payments": {
#       "Subscription Plans": {
#         "Basic Plan": "$10/month for 10GB storage.",
#         "Premium Plan": "$30/month for 100GB storage.",
#         "Enterprise Plan": "Custom pricing."
#       },
#       "Payment Methods": [
#         "Credit/Debit Card",
#         "PayPal",
#         "Bank Transfer (Enterprise Plan only)"
#       ],
#       "Refund Policy": "Payments are non-refundable unless stated otherwise."
#     },
#     "Termination": {
#       "Account Termination": "Users can terminate their account at any time.",
#       "Data Retention": "Data retained for 30 days post-termination."
#     },
#     "Limitation of Liability": {
#       "Liability Cap": "Total liability is limited to the amount paid in the last three months."
#     },
#     "Governing Law": {
#       "Jurisdiction": "Laws of New South Wales, Australia."
#     },
#     "Modifications": {
#       "Changes to Terms": "Terms may be modified at any time with notice."
#     },
#     "Contact Information": {
#       "Address": "Skyline Technologies Pty Ltd, 123 Digital Way, Level 5, Sydney, NSW, Australia",
#       "Email": "support@skyline.com",
#       "Phone": "+61 2 8000 1234"
#     }
#   }
# }
# ```INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# Now that I have summarized the key points of the terms and conditions, I need to analyze the risks associated with these terms.  
# Action: Analyze Risks  
# Action Input: (the summarized terms)  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# To proceed with the analysis, I would need the summarized terms and conditions text that you mentioned. Please provide that content so I can identify the risks and categorize the text accordingly.I need to provide the summarized terms and conditions text to analyze the risks.  
# Action: Analyze Risks  
# Action Input: ```json
# {
#   "Terms and Conditions Summary": {
#     "Introduction": {
#       "Effective Date": "December 1, 2024",
#       "Last Updated": "November 29, 2024",
#       "Provider": "Skyline Technologies Pty Ltd",
#       "Agreement": "By using the Service, you agree to these Terms."
#     },
#     "Eligibility": {
#       "Age Requirement": "Must be at least 18 years old.",
#       "Account Creation": "Accurate and current information is required."
#     },
#     "User Responsibilities": {
#       "Account Security": "Maintain confidentiality of account credentials.",
#       "Lawful Use": "Use the Service only for lawful purposes.",
#       "Prohibited Activities": [
#         "Harm or disrupt the Service.",
#         "Upload harmful software.",
#         "Harass or threaten others.",
#         "Gain unauthorized access."
#       ]
#     },
#     "User Content": {
#       "Ownership": "Users retain ownership of their content.",
#       "License": "Users grant Skyline a non-exclusive license to use their content."
#     },
#     "Intellectual Property": {
#       "Skyline Content": "All content provided by Skyline is protected by intellectual property laws."
#     },
#     "Privacy Policy": {
#       "Data Collection": "Personal information is collected for service delivery.",
#       "Data Protection": "Industry-standard encryption is used."
#     },
#     "Subscription and Payments": {
#       "Subscription Plans": {
#         "Basic Plan": "$10/month for 10GB storage.",
#         "Premium Plan": "$30/month for 100GB storage.",
#         "Enterprise Plan": "Custom pricing."
#       },
#       "Payment Methods": [
#         "Credit/Debit Card",
#         "PayPal",
#         "Bank Transfer (Enterprise Plan only)"
#       ],
#       "Refund Policy": "Payments are non-refundable unless stated otherwise."
#     },
#     "Termination": {
#       "Account Termination": "Users can terminate their account at any time.",
#       "Data Retention": "Data retained for 30 days post-termination."
#     },
#     "Limitation of Liability": {
#       "Liability Cap": "Total liability is limited to the amount paid in the last three months."
#     },
#     "Governing Law": {
#       "Jurisdiction": "Laws of New South Wales, Australia."
#     },
#     "Modifications": {
#       "Changes to Terms": "Terms may be modified at any time with notice."
#     },
#     "Contact Information": {
#       "Address": "Skyline Technologies Pty Ltd, 123 Digital Way, Level 5, Sydney, NSW, Australia",
#       "Email": "support@skyline.com",
#       "Phone": "+61 2 8000 1234"
#     }
#   }
# }
# ```  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# ```json
# {
#   "Risks": {
#     "Risk 1": {
#       "Description": "The limitation of liability clause caps the provider's liability to the amount paid in the last three months, which may not cover significant damages incurred by users.",
#       "Category": "Liability"
#     },
#     "Risk 2": {
#       "Description": "The terms allow for modifications at any time with notice, which could lead to unexpected changes that may adversely affect users without their consent.",
#       "Category": "Terms Modification"
#     },
#     "Risk 3": {
#       "Description": "The non-refundable payment policy may pose a risk for users who are dissatisfied with the service or who experience issues shortly after payment.",
#       "Category": "Financial"
#     }
#   }
# }
# ```INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# I have identified the risks associated with the terms and conditions. Now, I need to generate actionable recommendations based on these identified risks.  
# Action: Generate Recommendations  
# Action Input: ```json
# {
#   "Risks": {
#     "Risk 1": {
#       "Description": "The limitation of liability clause caps the provider's liability to the amount paid in the last three months, which may not cover significant damages incurred by users.",
#       "Category": "Liability"
#     },
#     "Risk 2": {
#       "Description": "The terms allow for modifications at any time with notice, which could lead to unexpected changes that may adversely affect users without their consent.",
#       "Category": "Terms Modification"
#     },
#     "Risk 3": {
#       "Description": "The non-refundable payment policy may pose a risk for users who are dissatisfied with the service or who experience issues shortly after payment.",
#       "Category": "Financial"
#     }
#   }
# }
# ```  INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# ```json
# {
#   "Recommendations": {
#     "Understand Liability Limits": "Before engaging with the service, carefully review the limitation of liability clause. Consider setting aside a contingency fund to cover potential damages that exceed the capped amount, ensuring you are financially prepared for any unforeseen issues.",
#     "Stay Informed on Terms Changes": "Regularly check for updates to the service terms and conditions. Consider subscribing to notifications or alerts from the provider to stay informed about any modifications that could impact your usage or rights.",
#     "Consider Payment Protection Options": "Explore payment protection options such as credit card chargebacks or third-party payment services that offer buyer protection. This can provide a safety net in case you are dissatisfied with the service or encounter issues shortly after payment."
#   }
# }
# ```INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
# I now know the final answer.  
# Final Answer: The terms and conditions from the provided URL outline the rules and responsibilities for using the Skyline Cloud Platform, including user eligibility, account security, ownership of user content, payment details, and limitations of liability. Key risks identified include limited liability for damages, potential for unexpected changes to terms, and a non-refundable payment policy. Recommendations for users include understanding liability limits, staying informed about changes to terms, and considering payment protection options.

# '''

# # Define a function to extract JSON objects
# def extract_json(data):
#     # Regular expression to find all JSON objects enclosed in ```json
#     json_objects = re.findall(r'```json(.*?)```', data, re.DOTALL)
    
#     # Parse the found JSON objects
#     parsed_json_objects = []
#     for json_obj in json_objects:
#         try:
#             parsed_json = json.loads(json_obj.strip())
#             parsed_json_objects.append(parsed_json)
#         except json.JSONDecodeError:
#             continue
    
#     return parsed_json_objects

# if __name__ == "__main__":
#     # Extract JSON objects
#     json_objects = extract_json(data)
    
#     # Initialize a list to hold separate JSON objects
#     extracted_json_list = []
    
#     # Append each JSON object to the list
#     for obj in json_objects:
#         extracted_json_list.append(obj)
    
#     # Print the list of JSON objects
#     for index, obj in enumerate(extracted_json_list, start=1):
#         print(f"JSON Object {index}:")
#         print(json.dumps(obj, indent=4))
#         print("-" * 40)




import re
import json

# The input data (your output as a string)
data = 

# Define a function to extract JSON objects
def extract_json(data):
    # Regular expression to find all JSON objects enclosed in ```json
    json_objects = re.findall(r'```json(.*?)```', data, re.DOTALL)
    
    # Parse the found JSON objects
    parsed_json_objects = []
    seen = set()  # To keep track of unique objects
    
    for json_obj in json_objects:
        try:
            # Parse JSON object
            parsed_json = json.loads(json_obj.strip())
            
            # Serialize the JSON object to a string with sorted keys for uniqueness check
            json_str = json.dumps(parsed_json, sort_keys=True)
            print(parsed_json_objects)
            # Add only distinct objects
            if json_str not in seen:
                seen.add(json_str)
                parsed_json_objects.append(parsed_json)
                
        except json.JSONDecodeError:
            continue
    
    return parsed_json_objects

if __name__ == "__main__":
    # Extract distinct JSON objects
    json_objects = extract_json(data)
    print(json_objects)
   
    # Print the list of distinct JSON objects
    # for index, obj in enumerate(json_objects, start=1):
    #     print(f"JSON Object {index}:")
    #     print(json.dumps(obj, indent=4))
    #     print("-" * 40)
