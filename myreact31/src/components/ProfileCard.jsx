import './ProfileCard.css';
// import ProfileImage from './img/member1.jpg';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faBars,
  faStickyNote,
  faEnvelope,
} from '@fortawesome/free-solid-svg-icons';
import { faFacebook } from '@fortawesome/free-brands-svg-icons';

function ProfileCard({
  profileImage,
  name,
  role,
  facebookurl,
  email,
  setPageName,
}) {
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
        <img src={profileImage} alt="프로필 이미지" />
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
        <a className="on" onClick={() => setPageName('member1')}></a>
        <a className="on" onClick={() => setPageName('member2')}></a>
        <a className="on" onClick={() => setPageName('member3')}></a>
        <a className="on" onClick={() => setPageName('member4')}></a>
      </nav>
    </section>
  );
}

export default ProfileCard;
