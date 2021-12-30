import PageLotto from './pages/PageLotto';
import ProfileCard from './components/ProfileCard';
import { useState } from 'react';
import memberList from './data/ProfileCard.json';
import ProfileImage1 from './img/member1.jpg';
import ProfileImage2 from './img/member2.jpg';
import ProfileImage3 from './img/member3.jpg';
import ProfileImage4 from './img/member4.jpg';

function App() {
  const [profileName, setProfileName] = useState('Elena');
  return (
    <>
      <h1>나현일</h1>
      <PageLotto />
      {memberList.map((member, index) => {
        if (profileName === member.name) {
          return (
            <div className={`member${(index % 4) + 1}`}>
              <ProfileCard
                profileImage={ProfileImage1}
                name={member.name}
                role={member.role}
                email={member.email}
                facebookurl={member.facebookurl}
                setPageName={setProfileName}
              />
            </div>
          );
        }
      })}
    </>
  );
}
// {pageName === 'member2' && (
//   <div className="member2">
//     <ProfileCard
//       profileImage={ProfileImage2}
//       name="Cristina"
//       role="CTO"
//       facebookurl="https://facebook.com/"
//       email="Cristina@Cristina.com"
//       className="on"
//       setPageName={setPageName}
//     />
//   </div>
// )}
// {pageName === 'member3' && (
//   <div className="member3">
//     <ProfileCard
//       profileImage={ProfileImage3}
//       name="Lucas"
//       role="CCO"
//       facebookurl="https://facebook.com/"
//       email="Lucas@Lucas.com"
//       className="on"
//       setPageName={setPageName}
//     />
//   </div>
// )}
// {pageName === 'member4' && (
//   <div className="member4">
//     <ProfileCard
//       profileImage={ProfileImage4}
//       name="Jacob"
//       role="CFO"
//       facebookurl="https://facebook.com/"
//       email="Jacob@Jacob.com"
//       className="on"
//       setPageName={setPageName}
//     />
//   </div>
// )}
//     </>
//   );
// }
export default App;
