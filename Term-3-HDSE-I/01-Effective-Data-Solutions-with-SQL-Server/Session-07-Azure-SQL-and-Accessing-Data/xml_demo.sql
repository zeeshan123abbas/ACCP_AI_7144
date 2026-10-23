-- Session 07: Typed and untyped XML
USE CampusDB;
GO
DROP TABLE IF EXISTS dbo.Applicant;
IF EXISTS (SELECT 1 FROM sys.xml_schema_collections WHERE name = 'ResumeSchema')
    DROP XML SCHEMA COLLECTION dbo.ResumeSchema;
GO
CREATE XML SCHEMA COLLECTION dbo.ResumeSchema AS N'
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="resume">
    <xs:complexType><xs:sequence>
      <xs:element name="skill" type="xs:string" maxOccurs="unbounded"/>
      <xs:element name="experience" type="xs:int"/>
    </xs:sequence></xs:complexType>
  </xs:element>
</xs:schema>';
GO
CREATE TABLE dbo.Applicant (
    ApplicantId INT IDENTITY PRIMARY KEY,
    Name     NVARCHAR(80),
    Notes    XML,
    Resume   XML(dbo.ResumeSchema)
);
INSERT INTO dbo.Applicant (Name, Notes, Resume) VALUES
(N'Sara', N'<note>Strong SQL</note>',
 N'<resume><skill>SQL</skill><skill>C#</skill><experience>2</experience></resume>');

SELECT Name,
       Resume.value('(/resume/experience)[1]', 'int') AS Years,
       Resume.exist('/resume/skill[.="C#"]')          AS KnowsCSharp
FROM dbo.Applicant;

SELECT a.Name, s.x.value('.', 'nvarchar(50)') AS Skill
FROM dbo.Applicant a
CROSS APPLY a.Resume.nodes('/resume/skill') AS s(x);

SELECT name, create_date FROM sys.xml_schema_collections WHERE name = 'ResumeSchema';
GO
