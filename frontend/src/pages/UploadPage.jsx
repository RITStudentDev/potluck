import { useState } from 'react';
import { useParams } from 'react-router-dom';
import '../css/UploadPage.css';

export default function UploadPage() {
    const { id } = useParams();
    const [files, setFiles] = useState([]);
    const [dragging, setDragging] = useState(false);

    // Handle files selected through the file dialogue
    const handleFileChange = (event) => {
        setFiles(Array.from(event.target.files));
    };

    // Handle files dragged into the drop zone
    const handleDrop = (event) => {
        event.preventDefault();
        setDragging(false);

        const droppedFiles = Array.from(event.dataTransfer.files);
        setFiles(droppedFiles);
    };

    // Prevent browser defaults
    const preventDefaults = (event) => {
        event.preventDefault();
        event.stopPropagation();
    };

    // Handle uploading
    const handleUpload = () => {
        if (files.length === 0) {
            alert('Please select a file to upload.');
            return;
        }

        // Implement upload logic here
        console.log('Uploading files:', files);
    };

    return (
        <>
            <h1 className="title">Upload Recipe</h1>
            <div className="container">
            <div className="upload-container">
                <label
                    htmlFor="file-input"
                    className={`drop-zone ${dragging ? 'drop-zone--over' : ''}`}
                    id="drop-zone"
                    onDragEnter={(e) => {
                        preventDefaults(e);
                        setDragging(true);
                    }}
                    onDragOver={(e) => {
                        preventDefaults(e);
                        setDragging(true);
                    }}
                    onDragLeave={(e) => {
                        preventDefaults(e);
                        setDragging(false);
                    }}
                    onDrop={handleDrop}
                >
                    <div className="drop-zone__prompt">
                        <span className="drop-zone__icon">📁</span>
                        <p>
                            Drag & drop your files here or{' '}
                            <strong>click to browse</strong>
                        </p>
                    </div>
                    <input
                        type="file"
                        id="file-input"
                        className="drop-zone__input"
                        name="myFile"
                        multiple
                        hidden
                        onChange={handleFileChange}
                    />
                </label>

                <div className="file-preview" id="file-preview">
                    {files.map((file, index) => (
                        <div className="file-item" key={`${file.name}-${index}`}>
                            <span>
                                📄 <strong>{file.name}</strong>{' '}
                                ({(file.size / 1024).toFixed(1)} KB)
                            </span>
                        </div>
                    ))}
                </div>
            </div>
            <textarea
                placeholder="Enter recipe name"
                className="recipe-name-input"
                rows="1"
            ></textarea>
            <textarea
                placeholder="Enter recipe description"
                className="recipe-description-input"
                rows="10"
            ></textarea>
            <textarea
                placeholder="Enter recipe ingredients"
                className="recipe-ingredients-input"
                rows="10"
            ></textarea>
        </div>
        </>
    );
}