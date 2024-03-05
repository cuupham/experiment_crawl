from pandas import DataFrame
import os


def create_df(df_form, filename):
    df = DataFrame(df_form)
    output_path = f"output/{filename}.xlsx"
    try:
        df.to_excel(output_path, index=False)
        if os.path.exists(output_path):
            print(f"Tạo file thành công: {output_path}")
        else:
            print("Có lôi khi tạo file.")
    except Exception as e:
        print(f"Có lỗi khi tạo file: {str(e)}")
