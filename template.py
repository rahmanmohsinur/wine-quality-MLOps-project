# /template.py

import os
import logging
from pathlib import Path


# ============================================================
# 1. LOGGING CONFIGURATION
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# ============================================================
# 2. PROJECT CONFIGURATION
# ============================================================

project_name = "mlProject"

project_root = Path.cwd()

# All paths are relative to the project root.
# This makes the template reusable in other projects.


# ============================================================
# 3. PROJECT DIRECTORY AND FILE STRUCTURE
# ============================================================

list_of_files = [

    # --------------------------------------------------------
    # GitHub workflows
    # --------------------------------------------------------

    ".github/workflows/.gitkeep",


    # --------------------------------------------------------
    # Data directories
    # --------------------------------------------------------

    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",


    # --------------------------------------------------------
    # Artifact and logging directories
    # --------------------------------------------------------

    "artifacts/.gitkeep",
    "logs/.gitkeep",


    # --------------------------------------------------------
    # Configuration files
    # --------------------------------------------------------

    "config.yaml",
    "params.yaml",
    "schema.yaml",


    # --------------------------------------------------------
    # Source package
    # --------------------------------------------------------

    f"src/{project_name}/__init__.py",


    # --------------------------------------------------------
    # Constants
    # --------------------------------------------------------

    f"src/{project_name}/constants/__init__.py",


    # --------------------------------------------------------
    # Core interfaces
    # --------------------------------------------------------

    f"src/{project_name}/core/__init__.py",
    f"src/{project_name}/core/pipeline_stage.py",
    f"src/{project_name}/core/config_manager.py",
    f"src/{project_name}/core/data_validator.py",
    f"src/{project_name}/core/model_evaluator.py",
    f"src/{project_name}/core/artifact_repository.py",


    # --------------------------------------------------------
    # Entities / Configuration domain
    # --------------------------------------------------------

    f"src/{project_name}/entities/__init__.py",
    f"src/{project_name}/entities/config_entity.py",
    f"src/{project_name}/entities/artifact_entity.py",
    f"src/{project_name}/entities/pipeline_entity.py",


    # --------------------------------------------------------
    # Configuration manager
    # --------------------------------------------------------

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",


    # --------------------------------------------------------
    # Machine Learning components
    # --------------------------------------------------------

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",


    # --------------------------------------------------------
    # Artifact repository implementation
    # --------------------------------------------------------

    f"src/{project_name}/repository/__init__.py",
    f"src/{project_name}/repository/local_artifact_repository.py",


    # --------------------------------------------------------
    # Pipeline orchestrator
    # --------------------------------------------------------

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stages.py",
    f"src/{project_name}/pipeline/pipeline_runner.py",


    # --------------------------------------------------------
    # Utilities
    # --------------------------------------------------------

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",


    # --------------------------------------------------------
    # Unit and integration tests
    # --------------------------------------------------------

    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",


    # --------------------------------------------------------
    # Research and experimentation
    # --------------------------------------------------------

    "research/trials.ipynb",


    # --------------------------------------------------------
    # Application entry points
    # --------------------------------------------------------

    "main.py",
    "app.py",
    "test.py",


    # --------------------------------------------------------
    # Deployment and project management
    # --------------------------------------------------------

    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    ".gitignore",
    "README.md",


    # --------------------------------------------------------
    # HTML templates
    # --------------------------------------------------------

    "templates/index.html",

]


# ============================================================
# 4. CREATE PROJECT DIRECTORIES AND FILES
# ============================================================

def create_project_structure():

    logging.info("Starting project structure generation...")

    created_directories = 0
    created_files = 0
    skipped_files = 0

    for filepath in list_of_files:

        file_path = project_root / filepath

        # ----------------------------------------------------
        # Create parent directories
        # ----------------------------------------------------

        file_directory = file_path.parent

        if not file_directory.exists():

            file_directory.mkdir(
                parents=True,
                exist_ok=True
            )

            created_directories += 1

            logging.info(
                f"Created directory: {file_directory}"
            )


        # ----------------------------------------------------
        # Create empty files without overwriting existing data
        # ----------------------------------------------------

        if not file_path.exists():

            file_path.touch()

            created_files += 1

            logging.info(
                f"Created file: {file_path}"
            )

        elif file_path.stat().st_size == 0:

            # File already exists but is empty.
            # touch() does not overwrite its contents.

            file_path.touch()

            skipped_files += 1

            logging.info(
                f"File already exists and is empty: {file_path}"
            )

        else:

            # Preserve existing file contents.

            skipped_files += 1

            logging.info(
                f"File already exists: {file_path}"
            )


    # ========================================================
    # 5. PROJECT GENERATION SUMMARY
    # ========================================================

    logging.info("=" * 60)

    logging.info("PROJECT STRUCTURE GENERATION COMPLETED")

    logging.info(f"Project name: {project_name}")

    logging.info(f"Project root: {project_root}")

    logging.info(f"Directories created: {created_directories}")

    logging.info(f"Files created: {created_files}")

    logging.info(f"Files skipped: {skipped_files}")

    logging.info("=" * 60)


# ============================================================
# 6. MAIN EXECUTION
# ============================================================

if __name__ == "__main__":

    create_project_structure()
