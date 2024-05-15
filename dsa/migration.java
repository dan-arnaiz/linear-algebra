/*
 * @author: dan-arnaiz
 * draft: 2021-05-10
 * 
 */

import java.sql.*;

public class Migration {
    public static void main(String[] args) {
        String sourceUrl = "jdbc:mysql://localhost:3306/sourceDB";
        String sourceUser = "sourceUser";
        String sourcePassword = "sourcePassword";

        String destinationUrl = "jdbc:mysql://localhost:3306/destinationDB";
        String destinationUser = "destinationUser";
        String destinationPassword = "destinationPassword";

        try {
            // Connect to source and destination databases
            Connection sourceConnection = DriverManager.getConnection(sourceUrl, sourceUser, sourcePassword);
            Connection destinationConnection = DriverManager.getConnection(destinationUrl, destinationUser, destinationPassword);

            // Create statement objects
            Statement sourceStatement = sourceConnection.createStatement();
            Statement destinationStatement = destinationConnection.createStatement();

            // Execute select query on source database
            ResultSet sourceResultSet = sourceStatement.executeQuery("SELECT * FROM sourceTable");

            // Get metadata of source table
            ResultSetMetaData metadata = sourceResultSet.getMetaData();
            int columnCount = metadata.getColumnCount();

            // Loop through the source result set
            while (sourceResultSet.next()) {
                StringBuilder insertQuery = new StringBuilder("INSERT INTO destinationTable VALUES (");

                // Loop through each column of the row
                for (int i = 1; i <= columnCount; i++) {
                    insertQuery.append("'").append(sourceResultSet.getString(i)).append("'");
                    if (i != columnCount) {
                        insertQuery.append(", ");
                    }
                }

                insertQuery.append(")");

                // Execute insert query on destination database
                destinationStatement.executeUpdate(insertQuery.toString());
            }

            // Close all connections and statements
            sourceResultSet.close();
            sourceStatement.close();
            sourceConnection.close();

            destinationStatement.close();
            destinationConnection.close();

            System.out.println("Data migration completed successfully.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}