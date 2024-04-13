-- Usage: sqlite3 climate_primate.db < protein_primate_brainimmu_thre80.sql

DROP TABLE protein_primate_brainimmu_thre80;
CREATE TABLE protein_primate_brainimmu_thre80 (
    Protein              TEXT    NOT NULL,
    Subject_sci_names    TEXT,
    Subject_common_names    TEXT,
    Subject_title    TEXT,
    Query_accuracy    TEXT,
    Subject_accuracy    TEXT,
    Percentage_identity    REAL,
    Alignment_length    INT,
    Mismatches    INT,
    Query_start    INT,
    Query_end    INT,
    Sequence_start    INT    NOT NULL,
    Sequence_end    INT,
    E_value    REAL,
    Bit_score    REAL,
    Percentage_query_coverage_per_subject    REAL,
    Percentage_query_coverage_per_hsp    REAL,
    query_sequence    TEXT,
    subject_sequence    TEXT,
    
    PRIMARY KEY (Protein, Subject_sci_names, Subject_title, Sequence_start)
);


