import { Component } from '@angular/core';
import {MatGridListModule} from '@angular/material/grid-list';
import { PortfolioService } from '../../service/portfolioService/portfolio.service';
import { CommonModule } from '@angular/common';
import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';

@Component({
  selector: 'app-painel',
  standalone: true,
  imports: [
    MatGridListModule,
    CommonModule,
    MatButtonModule,
    MatCardModule
  ],
  templateUrl: './painel.component.html',
  styleUrl: './painel.component.css'
})
export class PainelComponent {

  total:number = 0
  acao:number = 0
  bdr:number = 0
  fii:number = 0
  rendaFixa:number = 0
  outros:number = 0

  constructor(private _PortfolioService:PortfolioService){}

  ngOnInit(){

    this._PortfolioService.listarPortfolio().subscribe((data)=>{

      // maneira de criar o valor de cada ativo
      data.forEach((ativo)=>{
        ativo.valor = ativo.cotacao * ativo.quantidade
      })

      this.total = data.reduce((previousValue,currentValue) => previousValue + currentValue.valor,0)
      

      data.filter((ativo)=>{
        if (ativo.tipo == "Acoes"){
          this.acao += ativo.valor
        }
        if (ativo.tipo == "Brazilian Depositary Receipts"){
          this.bdr += ativo.valor
        }
        if (ativo.tipo == "Fundo de Investimento"){
          this.fii += ativo.valor
        }
        if (ativo.tipo == "Tesouro Direto"){
          this.rendaFixa += ativo.valor
        }
        if (ativo.tipo == "Outros"){
          this.outros += ativo.valor
        }
        
        
      })

      
    })

  }

  

}
