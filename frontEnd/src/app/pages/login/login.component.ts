import { Component, viewChild } from '@angular/core';
import { AuthServiceService } from '../../service/authService/auth-service.service';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { NavBarComponent } from '../../componentes/nav-bar/nav-bar.component';




@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    FormsModule,
    RouterLink,
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  usuario: string = ''
  senha: string = ''
  alerta: string = ''

  constructor(
    private _AuthServiceService: AuthServiceService,
    private _Router: Router,

  ) { }

  ngOnInit() { }

  login() {

    this._AuthServiceService.login(this.usuario, this.senha).subscribe(
      (data) => {
        console.log(data)
        if (data && data['auth_token']) {
          this._AuthServiceService.storeToken(data['auth_token'])
          console.log('Login bem sucedido')
          this._Router.navigate(['portfolio/'])

        }

      }, (error) => {
        this.alerta = '* Usuário ou senha incorreta'
      }
    )
  }

}
