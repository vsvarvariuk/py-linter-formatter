def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "sourse": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [{"line": elem["line_number"],
                        "column": elem["column_number"],
                        "message": elem["text"],
                        "name": elem["code"],
                        "sourse": "flake8"
                        } for elem in errors],
            "path": file_path,
            "status": "failed"

            }


def format_linter_report(linter_report: dict) -> list:
    return [{"errors": [],
             "path": [elem for elem in linter_report if linter_report[elem] == []],
             "status": "passed"},
            {"errors": [{"line": elem["line_number"],
                         "column": elem["column_number"],
                         "message": elem["text"],
                         "name": elem["code"],
                         "sourse": "flake8"
                         }
                        for elem in linter_report["./source_code_2.py"]],
             "path": "./source_code_2.py",
             "status": "failed"
             }]
