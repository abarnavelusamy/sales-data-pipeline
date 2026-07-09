from datetime import datetime


def generate_html_report(checkpoint_result, report_name):

    html = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <title>Validation Report</title>

        <style>

            body {{
                font-family: Arial;
                margin:40px;
                background:#f4f4f4;
            }}

            h1 {{
                color:#1F4E79;
            }}

            table {{

                border-collapse: collapse;

                width:100%;

                background:white;

            }}

            th,td {{

                border:1px solid #ccc;

                padding:10px;

                text-align:center;

            }}

            th {{

                background:#1F4E79;

                color:white;

            }}

            .success {{

                color:green;

                font-weight:bold;

            }}

            .failed {{

                color:red;

                font-weight:bold;

            }}

        </style>

    </head>

    <body>

    <h1>Sales Data Pipeline Validation Report</h1>

    <p><b>Run ID :</b> {checkpoint_result["run_id"]}</p>

    <p><b>Generated :</b> {datetime.now()}</p>

    <table>

    <tr>

        <th>Table</th>

        <th>Total Rules</th>

        <th>Passed</th>

        <th>Failed</th>

        <th>Status</th>

    </tr>

    """

    for result in checkpoint_result["results"]:

        status = "PASS" if result["success"] else "FAIL"

        css = "success" if result["success"] else "failed"

        html += f"""

        <tr>

            <td>{result["table"]}</td>

            <td>{result["total_rules"]}</td>

            <td>{result["passed"]}</td>

            <td>{result["failed"]}</td>

            <td class="{css}">{status}</td>

        </tr>

        """

    html += """

    </table>

    </body>

    </html>

    """

    with open(report_name, "w") as file:

        file.write(html)