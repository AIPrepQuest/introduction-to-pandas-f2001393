import pandas as pd
from main import analyze_data

def test_analyze_data(tmp_path):
    csv_data = "A,B,C\n1,2,3\n4,5,6\n7,8,9"
    test_file = tmp_path / "data.csv"
    test_file.write_text(csv_data)

    result = analyze_data(test_file)

    assert result['num_rows'] == 3
    assert result['num_columns'] == 3
    assert result['column_with_max_mean'] == 'C'
