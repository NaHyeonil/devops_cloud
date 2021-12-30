import './ProfileCard.css';
import ProfileImage from '../img/member1.jpg';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faBars,
  faStickyNote,
  faEnvelope,
} from '@fortawesome/free-solid-svg-icons';
import { faFacebook } from '@fortawesome/free-brands-svg-icons';

function ProfileCard({ name, role, facebookurl, email, setPageName }) {
  return (
    <section>
      <nav className="menu">
        <a href="#">
          <FontAwesomeIcon icon={faBars} />
        </a>
        <a href="#">
          <FontAwesomeIcon icon={faStickyNote} />
        </a>
      </nav>
      <article className="profile">
        <img src={ProfileImage} alt="프로필 이미지" />
        <h1>{name}</h1>
        <h2>{role}</h2>
        <a href="#" class="btnView">
          ViewMore
        </a>
      </article>

      <ul class="contact">
        <li>
          <i className="fab fa-facebook-f"></i>
          <a href={facebookurl} target="_blank">
            <FontAwesomeIcon icon={faFacebook} />
            {facebookurl}
          </a>
        </li>
        <li>
          <i className="fas fa-envelope"></i>
          <span>
            <FontAwesomeIcon icon={faEnvelope} />
            {email}
          </span>
        </li>
      </ul>
      <nav className="others">
        <a className="on" onClick={() => setPageName('Elena')}></a>
        <a className="on" onClick={() => setPageName('Cristina')}></a>
        <a className="on" onClick={() => setPageName('Lucas')}></a>
        <a className="on" onClick={() => setPageName('Jacob')}></a>
        <a className="on" onClick={() => setPageName('Jacob123')}></a>
      </nav>
    </section>
  );
}

export default ProfileCard;
