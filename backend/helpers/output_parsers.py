# helpers/output_parsers.py

class SummaryOutputParser:
    def parse(self, text: str) -> dict:
        """
        Parse the text output into a structured dictionary (JSON format).
        Assumes the text follows a specific pattern with sections like:
        Overview, Key Clauses, etc.
        """
        try:
            summary = {
                "overview": "",
                "key_clauses": {},
                "ambiguities": [],
                "risks_legal_implications": [],
                "recommendations": []
            }

            lines = text.split("\n")

            # Example parsing logic to break text into sections
            section = None
            for line in lines:
                line = line.strip()
                if line.startswith("Overview"):
                    section = "overview"
                elif line.startswith("Key Clauses"):
                    section = "key_clauses"
                elif line.startswith("Ambiguities"):
                    section = "ambiguities"
                elif line.startswith("Risks and Legal Implications"):
                    section = "risks_legal_implications"
                elif line.startswith("Recommendations"):
                    section = "recommendations"

                # Append content to the appropriate section
                if section:
                    summary[section] += line + " "

            return summary
        except Exception as e:
            return {"error": f"Error parsing the summary: {str(e)}"}
