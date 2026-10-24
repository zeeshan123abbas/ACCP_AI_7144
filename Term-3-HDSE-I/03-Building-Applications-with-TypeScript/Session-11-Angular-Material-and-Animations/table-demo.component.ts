// table-demo.component.ts - a Material data table
import { Component } from '@angular/core';
import { MatTableModule } from '@angular/material/table';

interface Student {
  roll: number;
  name: string;
  marks: number;
}

@Component({
  selector: 'app-table-demo',
  standalone: true,
  imports: [MatTableModule],
  template: `
    <h3>Table</h3>
    <table mat-table [dataSource]="students">
      <!-- each ng-container defines ONE column -->
      <ng-container matColumnDef="roll">
        <th mat-header-cell *matHeaderCellDef>Roll</th>
        <td mat-cell *matCellDef="let s">{{ s.roll }}</td>
      </ng-container>
      <ng-container matColumnDef="name">
        <th mat-header-cell *matHeaderCellDef>Name</th>
        <td mat-cell *matCellDef="let s">{{ s.name }}</td>
      </ng-container>
      <ng-container matColumnDef="marks">
        <th mat-header-cell *matHeaderCellDef>Marks</th>
        <td mat-cell *matCellDef="let s">{{ s.marks }}</td>
      </ng-container>

      <!-- which columns to show, and in what order -->
      <tr mat-header-row *matHeaderRowDef="columns"></tr>
      <tr mat-row *matRowDef="let row; columns: columns"></tr>
    </table>
  `,
})
export class TableDemoComponent {
  columns = ['roll', 'name', 'marks'];
  students: Student[] = [
    { roll: 1, name: 'Ali', marks: 88 },
    { roll: 2, name: 'Mahnoor', marks: 93 },
    { roll: 3, name: 'Saad', marks: 71 },
  ];
}
