import unittest
from main import retrieve_data, write_output_to_file


class CustomTest(unittest.TestCase):
    def test_process_valid_file(self) -> None:
        """Tests process valid file"""

        data = retrieve_data(input_file_path="data/data_1.json")
        self.assertIsInstance(data, dict)

    def test_process_valid_file_and_write_to_output(self) -> None:
        """Tests process valid file and write to output file"""

        data = retrieve_data("data/data_1.json")
        self.assertTrue(
            write_output_to_file(output_file_path="test_data/output.json", data=data)
        )

    def test_process_non_existent_file(self) -> None:
        """Tests process non existent file"""

        with self.assertRaises(FileNotFoundError):
            retrieve_data("file.json")

    def test_process_invalid_file_content(self) -> None:
        """Tests process invalid file content"""

        with self.assertRaises(TypeError):
            retrieve_data("test_data/invalid.json")


if __name__ == "__main__":
    unittest.main()
