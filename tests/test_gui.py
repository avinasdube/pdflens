import unittest
from unittest.mock import patch, MagicMock
from src.pdf_processing import open_pdf
from src.utils import save_text, clear_text, search_and_highlight
from main import PDFtoTextApp  

class TestPDFtoTextApp(unittest.TestCase):

    def setUp(self):
        """Set up the app for testing."""
        self.app = PDFtoTextApp()
        self.app.update()  # Ensure the GUI is initialized

    def tearDown(self):
        """Destroy the app after testing."""
        self.app.destroy()

    def test_banner_wraplength_adjustment(self):
        """Test if the banner wrap length adjusts correctly."""
        self.app.geometry("1000x500")
        self.app.adjust_banner_wraplength()
        expected_wraplength = 1000 - 40
        self.assertEqual(self.app.banner.cget("wraplength"), expected_wraplength)

    @patch("src.pdf_processing.open_pdf")
    def test_open_pdf_action(self, mock_open_pdf):
        """Test the open_pdf_action method."""
        self.app.open_pdf_action()
        mock_open_pdf.assert_called_once_with(self.app.text_box)

    @patch("src.utils.search_and_highlight")
    def test_search_text_action(self, mock_search_and_highlight):
        """Test the search_text_action method."""
        test_query = "sample"
        self.app.search_bar.insert(0, test_query)  # Simulate entering a query
        self.app.search_text_action()
        mock_search_and_highlight.assert_called_once_with(self.app.text_box, test_query)

    @patch("src.utils.save_text")
    def test_save_text_action(self, mock_save_text):
        """Test the save_text_action method."""
        self.app.save_text_action()
        mock_save_text.assert_called_once_with(self.app.text_box)

    @patch("src.utils.clear_text")
    def test_clear_text_action(self, mock_clear_text):
        """Test the clear_text_action method."""
        self.app.clear_text_action()
        mock_clear_text.assert_called_once_with(self.app.text_box)

    def test_gui_elements_exist(self):
        """Test if all main GUI elements are present."""
        self.assertIsNotNone(self.app.file_button, "Open PDF button is missing.")
        self.assertIsNotNone(self.app.search_bar, "Search bar is missing.")
        self.assertIsNotNone(self.app.search_button, "Search button is missing.")
        self.assertIsNotNone(self.app.text_box, "Text box is missing.")
        self.assertIsNotNone(self.app.save_button, "Save button is missing.")
        self.assertIsNotNone(self.app.clear_button, "Clear button is missing.")
        self.assertIsNotNone(self.app.footer, "Footer is missing.")

    def test_initial_window_configuration(self):
        """Test initial window properties."""
        self.assertEqual(self.app.title(), "PDF Lens")
        self.assertGreaterEqual(self.app.winfo_width(), 300)
        self.assertGreaterEqual(self.app.winfo_height(), 420)

    @patch("PIL.Image.open")
    def test_icon_loading(self, mock_image_open):
        """Test if icons are loaded correctly."""
        mock_image_open.return_value = MagicMock()
        self.assertIsNotNone(self.app.file_button.cget("image"), "File button image is not loaded.")
        self.assertIsNotNone(self.app.save_button.cget("image"), "Save button image is not loaded.")
        self.assertIsNotNone(self.app.clear_button.cget("image"), "Clear button image is not loaded.")
        self.assertIsNotNone(self.app.search_button.cget("image"), "Search button image is not loaded.")

if __name__ == "__main__":
    unittest.main()
