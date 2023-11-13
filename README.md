# Dataset - Greek  Parliament Debates to Open Linked Data

This is the repository for the Dataset of [Greek Parliament Debates to Open Linked Data](https://github.com/john-papani/diploma). In this repository, you will find the necessary data and resources related to the project. 

## Project Structure

The repository is structured as follows:
- ### [`raw_text_data/`](https://github.com/john-papani/diploma_dataset/tree/master/raw_text_data)
    >This directory contains the raw text data used in the project. You can find the original text files of the Greek Parliament debates in this folder. (format: docx, doc, txt)

    - ### [`year2022_2023/`](https://github.com/john-papani/diploma_dataset/tree/master/raw_text_data/year2022-23): This directory contains additional raw text data.
        - [`year2022until10nov23/`](https://github.com/john-papani/diploma_dataset/tree/master/raw_text_data/year2022-23/year2022until10nov23): New files containing debates data for the period until November 10, 2023.
        - [`harvester.db`](https://github.com/john-papani/diploma_dataset/blob/master/raw_text_data/year2022-23/harvester.db): SQLite database file storing additional processed data.
        - [`praktikaVoulis10_12_2022.csv`](https://github.com/john-papani/diploma_dataset/blob/master/raw_text_data/year2022-23/praktikaVoulis10_12_2022.csv): CSV file with details for the new files.
        - [`praktikaVoulis10_12_2022.json`](https://github.com/john-papani/diploma_dataset/blob/master/raw_text_data/year2022-23/praktikaVoulis10_12_2022.json): JSON file with details for the new files.

    - ### [`sqlite_database.db`](https://github.com/john-papani/diploma_dataset/blob/master/sqlite_database.db)
        >This SQLite database file stores the processed and transformed data from the raw text files. The data is structured and organized within this database, making it easier to query and analyze.

---
## Usage Guidelines
- **Data Integrity:** While efforts have been made to ensure the accuracy of the data, please note that no dataset is perfect. Verify the data according to your use case requirements.
- **Contribution:** If you find issues with the dataset or have improvements to suggest, feel free to open an issue or create a pull request.
- **Attribution:** If you use this dataset in your research or applications, please provide appropriate attribution to this repository.