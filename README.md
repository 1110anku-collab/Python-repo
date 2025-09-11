# File Organizer

A Python script that automatically organizes files in a target directory based on file types, moving them into categorized folders for better file management.

## Features

- **Automatic File Classification**: Organizes files into predefined categories based on file extensions
- **Multiple File Categories**: Documents, Images, Videos, Audio, Archives, Code, and Others
- **Smart Conflict Resolution**: Handles duplicate file names by adding counters
- **Comprehensive Logging**: Detailed logs with configurable levels (DEBUG, INFO, WARNING, ERROR)
- **Dry Run Mode**: Preview changes without actually moving files
- **Statistics Tracking**: Detailed reports on organization results
- **Error Handling**: Robust exception handling for various scenarios
- **Cross-Platform**: Works on Windows, macOS, and Linux

## File Categories

The script organizes files into the following categories:

### Documents
- PDF, Word docs (.docx, .doc), Text files (.txt), RTF
- Spreadsheets (.xlsx, .xls), Presentations (.pptx, .ppt)
- CSV, JSON, XML, Markdown (.md), LaTeX (.tex)

### Images  
- Common formats: JPG, PNG, GIF, BMP, TIFF, SVG, WebP
- RAW formats: CR2, NEF, ORF, SR2

### Videos
- MP4, AVI, MKV, MOV, WMV, FLV, WebM
- MPEG, 3GP, OGV, TS, F4V

### Audio
- MP3, WAV, FLAC, AAC, OGG, WMA
- M4A, OPUS, AIFF, AU, RA, AMR

### Archives
- ZIP, RAR, 7Z, TAR, GZ, BZ2, XZ
- ISO, DMG, PKG, DEB, RPM

### Code
- Programming languages: Python, JavaScript, HTML, CSS, Java, C/C++
- PHP, Ruby, Go, Rust, Swift, Kotlin, TypeScript
- SQL, SCSS, LESS

### Others
- Any file type not matching the above categories

## Installation

1. **Requirements**: Python 3.6 or higher (uses only built-in libraries)

2. **Download the script**:
   ```bash
   git clone <repository-url>
   cd file-organizer
   ```

3. **Make executable** (optional on Unix systems):
   ```bash
   chmod +x file_organizer.py
   ```

## Usage

### Basic Usage
```bash
python file_organizer.py /path/to/messy/folder
```

### Advanced Usage
```bash
# Preview changes without moving files
python file_organizer.py ~/Downloads --dry-run

# Enable debug logging
python file_organizer.py ./documents --log-level DEBUG

# Quiet mode (warnings and errors only)
python file_organizer.py /path/to/folder --log-level WARNING
```

### Command Line Options

- `directory`: Path to the directory to organize (required)
- `--dry-run`: Preview what would be organized without moving files
- `--log-level`: Set logging level (DEBUG, INFO, WARNING, ERROR) - default: INFO

## Examples

### Example 1: Organize Downloads Folder
```bash
python file_organizer.py ~/Downloads
```
This will:
- Create category folders in ~/Downloads
- Move files to appropriate folders
- Generate logs and statistics

### Example 2: Preview Changes
```bash
python file_organizer.py /messy/folder --dry-run
```
Shows what would happen without actually moving files.

### Example 3: Verbose Logging
```bash
python file_organizer.py ./documents --log-level DEBUG
```
Provides detailed information about each operation.

## Output Structure

After running the script, your directory will be organized like this:

```
Target Directory/
├── Documents/
│   ├── report.pdf
│   ├── spreadsheet.xlsx
│   └── notes.txt
├── Images/
│   ├── photo1.jpg
│   ├── screenshot.png
│   └── logo.svg
├── Videos/
│   ├── movie.mp4
│   └── presentation.mov
├── Audio/
│   ├── song.mp3
│   └── podcast.wav
├── Archives/
│   ├── backup.zip
│   └── installer.tar.gz
├── Code/
│   ├── script.py
│   ├── webpage.html
│   └── styles.css
├── Others/
│   └── unknown_file.xyz
└── logs/
    └── file_organizer_YYYYMMDD_HHMMSS.log
```

## Logging

The script creates detailed logs in the `logs/` directory with timestamps:
- File operations (move, create folders)
- Errors and warnings
- Final statistics and success rates
- Timestamp: `file_organizer_YYYYMMDD_HHMMSS.log`

## Safety Features

1. **Dry Run Mode**: Test before making changes
2. **Duplicate Handling**: Files with same names get numbered suffixes
3. **Hidden File Protection**: Skips system and hidden files
4. **Permission Handling**: Graceful error handling for permission issues
5. **Comprehensive Logging**: Full audit trail of all operations

## Error Handling

The script handles various error scenarios:
- Permission denied errors
- File system errors (disk full, etc.)
- Invalid directory paths
- File conflicts and naming issues
- Interrupted operations

## Statistics and Reporting

After completion, you'll see:
- Total files processed
- Files organized by category
- Success rate percentage  
- Error count and details
- Execution time and performance metrics

## Troubleshooting

### Common Issues

1. **Permission Denied**:
   - Run with appropriate permissions
   - Check if files are in use by other programs

2. **Directory Not Found**:
   - Verify the path exists
   - Use absolute paths for clarity

3. **Disk Space**:
   - Ensure sufficient disk space
   - Consider using dry-run first

### Getting Help

- Use `--help` flag for command line options
- Check log files for detailed error information
- Run with `--log-level DEBUG` for maximum detail

## Development

The script is structured as a class-based solution with the following components:

- `FileOrganizer` class: Main organizing logic
- Category definitions: Extensible file type mappings
- Logging system: Comprehensive activity tracking
- Statistics tracking: Performance and success metrics
- Command-line interface: User-friendly argument parsing

## Contributing

To extend the script:
1. Add new file extensions to `self.file_categories`
2. Create new categories by adding to the dictionary
3. Modify logging levels or formats as needed
4. Add new command-line options in the `main()` function

## License

This project is open source. Feel free to modify and distribute.

## Version History

- **v1.0** (2024): Initial release with full organizing functionality
  - File type classification
  - Category-based organization  
  - Logging and statistics
  - Dry run mode
  - Error handling
